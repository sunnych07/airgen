// AirGen Aviation - Figma Automation Script
// Run this script in Figma via the "Scripter" plugin or Figma Plugin Developer Console.
// It generates all 6 presentation frames (1440x900), color tokens, and layout components.

async function createAirgenDesignSystem() {
  await figma.loadFontAsync({ family: "Inter", style: "Regular" });
  await figma.loadFontAsync({ family: "Inter", style: "Bold" });

  // 1. Color Palette Tokens
  const colors = {
    bgDark: { r: 7/255, g: 18/255, b: 36/255 },       // #071224
    surface: { r: 10/255, g: 29/255, b: 60/255 },     // #0A1D3C
    card: { r: 13/255, g: 34/255, b: 69/255 },        // #0D2245
    border: { r: 30/255, g: 58/255, b: 138/255 },     // #1E3A8A
    cyan: { r: 56/255, g: 189/255, b: 248/255 },      // #38BDF8
    gold: { r: 251/255, g: 191/255, b: 36/255 },      // #FBBF24
    emerald: { r: 16/255, g: 185/255, b: 129/255 },   // #10B981
    white: { r: 1, g: 1, b: 1 },
    muted: { r: 148/255, g: 163/255, b: 184/255 },    // #94A3B8
  };

  const screens = [
    { id: "01", name: "Screen 1 - Hero & Trust Anchor", subtitle: "From 12th Grade to Airline Flight Deck" },
    { id: "02", name: "Screen 2 - 5-Stage Pilot Flightpath", subtitle: "Eligibility to First Officer Seat" },
    { id: "03", name: "Screen 3 - 12th Eligibility & ROI Calculator", subtitle: "Interactive Regulatory Clearance" },
    { id: "04", name: "Screen 4 - Global Fleet & Bases", subtitle: "USA Phoenix, South Africa & India HQ" },
    { id: "05", name: "Screen 5 - 80+ Alumni Hall of Wings", subtitle: "IndiGo, Air India, Akasa Placements" },
    { id: "06", name: "Screen 6 - Parental Admissions & FAQs", subtitle: "1-on-1 Airline Captain Counseling" },
  ];

  let xOffset = 0;

  for (let i = 0; i < screens.length; i++) {
    const s = screens[i];
    
    // Create Artboard Frame (1440 x 900 Desktop Standard)
    const frame = figma.createFrame();
    frame.name = `AirGen - ${s.name}`;
    frame.resize(1440, 900);
    frame.x = xOffset;
    frame.y = 0;
    frame.fills = [{ type: 'SOLID', color: colors.bgDark }];
    frame.cornerRadius = 0;

    // Header Bar
    const header = figma.createFrame();
    header.name = "Top Navigation Bar";
    header.resize(1280, 64);
    header.x = 80;
    header.y = 24;
    header.fills = [{ type: 'SOLID', color: colors.card }];
    header.cornerRadius = 16;
    header.strokes = [{ type: 'SOLID', color: colors.border }];
    header.strokeWeight = 1;

    // Brand Logo in Header
    const brandText = figma.createText();
    brandText.characters = "AIRGEN AVIATION";
    brandText.fontName = { family: "Inter", style: "Bold" };
    brandText.fontSize = 18;
    brandText.fills = [{ type: 'SOLID', color: colors.white }];
    brandText.x = 24;
    brandText.y = 22;
    header.appendChild(brandText);

    // 80+ Alumni Badge in Header
    const alumniBadge = figma.createText();
    alumniBadge.characters = "80+ Graduated Pilots Flying Lines";
    alumniBadge.fontName = { family: "Inter", style: "Bold" };
    alumniBadge.fontSize = 12;
    alumniBadge.fills = [{ type: 'SOLID', color: colors.gold }];
    alumniBadge.x = 240;
    alumniBadge.y = 25;
    header.appendChild(alumniBadge);

    frame.appendChild(header);

    // Screen Title & Subtitle
    const title = figma.createText();
    title.characters = s.name;
    title.fontName = { family: "Inter", style: "Bold" };
    title.fontSize = 32;
    title.fills = [{ type: 'SOLID', color: colors.white }];
    title.x = 80;
    title.y = 120;
    frame.appendChild(title);

    const subtitle = figma.createText();
    subtitle.characters = s.subtitle;
    subtitle.fontName = { family: "Inter", style: "Regular" };
    subtitle.fontSize = 16;
    subtitle.fills = [{ type: 'SOLID', color: colors.cyan }];
    subtitle.x = 80;
    subtitle.y = 165;
    frame.appendChild(subtitle);

    // Slide Footer Watermark (Mandatory AirGen Branding)
    const watermark = figma.createText();
    watermark.characters = `AIRGEN AVIATION • SCREEN ${s.id} • CONFIDENTIAL COMPETITION DESIGN JURY PRESENTATION`;
    watermark.fontName = { family: "Inter", style: "Bold" };
    watermark.fontSize = 11;
    watermark.fills = [{ type: 'SOLID', color: colors.muted }];
    watermark.x = 80;
    watermark.y = 860;
    frame.appendChild(watermark);

    figma.currentPage.appendChild(frame);

    xOffset += 1600; // 1440 + 160px gap between screens
  }

  figma.viewport.scrollAndZoomIntoView(figma.currentPage.children);
  figma.notify("✈️ AirGen Aviation Design System & 6 Master Screens successfully generated!");
}

createAirgenDesignSystem();
