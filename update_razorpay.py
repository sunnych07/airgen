import re

with open(r'C:\airgen\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add Razorpay Script to head
if "checkout.razorpay.com" not in content:
    content = content.replace('</head>', '    <script src="https://checkout.razorpay.com/v1/checkout.js"></script>\n</head>')

# 2. Add JS logic for Payment
payment_js = """
        async function payWithRazorpay(courseName, amountInRupees, btnId) {
            if (!isLoggedIn) {
                alert("Please login first to enroll and pay.");
                showPage('register');
                return;
            }
            
            const btn = document.getElementById(btnId);
            const originalText = btn.innerText;
            btn.innerText = "Processing secure payment...";
            btn.disabled = true;
            
            try {
                // 1. Get Order ID from Python Backend
                const res = await fetch('/api/create_order', {
                    method: 'POST',
                    body: JSON.stringify({ amount: amountInRupees * 100 }) 
                });
                const data = await res.json();
                
                if (data.success) {
                    // 2. Open Razorpay Checkout
                    var options = {
                        "key": "rzp_live_TZ4lxunOpCOa6H", 
                        "amount": amountInRupees * 100,
                        "currency": "INR",
                        "name": "Airgen Aviation",
                        "description": "Enrollment for: " + courseName,
                        "image": "https://images.unsplash.com/photo-1540962351504-03099e0a754b?q=80&w=200",
                        "order_id": data.order_id,
                        "handler": function (response){
                            alert("Payment Successful! Welcome to Airgen Aviation.\\nPayment ID: " + response.razorpay_payment_id);
                            btn.innerText = "Enrolled ✓";
                            btn.style.background = "#10B981";
                            btn.style.color = "white";
                        },
                        "prefill": {
                            "email": loggedInEmail
                        },
                        "theme": {
                            "color": "#E11D48"
                        }
                    };
                    var rzp1 = new Razorpay(options);
                    rzp1.on('payment.failed', function (response){
                        alert("Payment Failed: " + response.error.description);
                    });
                    rzp1.open();
                } else {
                    alert("Failed to initialize payment gateway.");
                }
            } catch (e) {
                alert("Network error. Please try again.");
            } finally {
                if(btn.innerText !== "Enrolled ✓") {
                    btn.innerText = originalText;
                    btn.disabled = false;
                }
            }
        }
"""
content = content.replace('function toggleTheme()', payment_js + '\n        function toggleTheme()')


# 3. Update Course Buttons
old_btn_1 = """<button onclick="toggleChat()" style="background: white; color: black; padding: 1rem 1.5rem; border: none; border-radius: 3rem; font-weight: 800; cursor: pointer; width: 100%; transition: 0.3s;" onmouseover="this.style.background='#E11D48'; this.style.color='white'" onmouseout="this.style.background='white'; this.style.color='black'">Enquire Now</button>"""
new_btn_1 = """<button id="payBtn1" onclick="payWithRazorpay('Zero to CPL Pathway', 50000, 'payBtn1')" style="background: white; color: black; padding: 1rem 1.5rem; border: none; border-radius: 3rem; font-weight: 800; cursor: pointer; width: 100%; transition: 0.3s; margin-bottom: 0.5rem;" onmouseover="this.style.background='#E11D48'; this.style.color='white'" onmouseout="this.style.background='white'; this.style.color='black'">Enroll & Pay Advance (₹50,000)</button>
<button onclick="toggleChat()" style="background: transparent; color: #E11D48; border: 1px solid #E11D48; padding: 0.8rem 1.5rem; border-radius: 3rem; font-weight: 800; cursor: pointer; width: 100%;">Enquire First</button>"""

old_btn_2 = """<button onclick="toggleChat()" style="background: white; color: black; padding: 1rem 1.5rem; border: none; border-radius: 3rem; font-weight: 800; cursor: pointer; width: 100%; transition: 0.3s;" onmouseover="this.style.background='#38BDF8'; this.style.color='white'" onmouseout="this.style.background='white'; this.style.color='black'">Enquire Now</button>"""
new_btn_2 = """<button id="payBtn2" onclick="payWithRazorpay('Type Rating & MCC', 25000, 'payBtn2')" style="background: white; color: black; padding: 1rem 1.5rem; border: none; border-radius: 3rem; font-weight: 800; cursor: pointer; width: 100%; transition: 0.3s; margin-bottom: 0.5rem;" onmouseover="this.style.background='#38BDF8'; this.style.color='white'" onmouseout="this.style.background='white'; this.style.color='black'">Enroll & Pay Advance (₹25,000)</button>
<button onclick="toggleChat()" style="background: transparent; color: #38BDF8; border: 1px solid #38BDF8; padding: 0.8rem 1.5rem; border-radius: 3rem; font-weight: 800; cursor: pointer; width: 100%;">Enquire First</button>"""

content = content.replace(old_btn_1, new_btn_1)
content = content.replace(old_btn_2, new_btn_2)

with open(r'C:\airgen\index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Added Razorpay Frontend.")
