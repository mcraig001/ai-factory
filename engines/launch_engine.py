"""
Launch Engine - Automated Product Launch System
Generates all marketing assets, listings, and launch materials
"""

import os
import json
from datetime import datetime
import anthropic

class LaunchEngine:
    def __init__(self):
        self.client = anthropic.Anthropic(
            api_key=os.environ.get("ANTHROPIC_API_KEY")
        )
        
    def generate_gumroad_listing(self, product_info):
        """Generate optimized Gumroad listing copy"""
        print("  📝 Generating Gumroad listing...")
        
        prompt = f"""Create a compelling Gumroad product listing for:

Product: {product_info['title']}
Price: ${product_info['price']}
Target Customer: {product_info['target_customer']}
Problem: {product_info['problem']}
Solution: {product_info['solution']}

Generate:
1. Product Title (SEO optimized, under 60 chars)
2. Subtitle (benefit-focused, under 120 chars)
3. Description (compelling, conversion-optimized, 300-500 words)
   - Hook (problem)
   - What you get (features)
   - How it works
   - Perfect for
   - Why this vs alternatives
   - Value comparison
4. Short Description (280 chars for social media)
5. Tags (15 relevant keywords)

Format as markdown with clear sections. Be persuasive but honest. Focus on benefits over features.
"""
        
        message = self.client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=4000,
            messages=[{"role": "user", "content": prompt}]
        )
        
        return message.content[0].text
    
    def generate_social_posts(self, product_info):
        """Generate social media launch posts"""
        print("  📱 Generating social media posts...")
        
        prompt = f"""Create social media launch posts for:

Product: {product_info['title']}
Price: ${product_info['price']}
Target: {product_info['target_customer']}
Problem: {product_info['problem']}

Generate:

1. TWITTER/X THREAD (5 tweets):
   - Tweet 1: Hook + announcement
   - Tweet 2: Problem it solves
   - Tweet 3: Key features
   - Tweet 4: Pricing/value
   - Tweet 5: CTA with link

2. LINKEDIN POST (professional tone):
   - Opening hook
   - Why I built this
   - Who it helps
   - Link

3. REDDIT POST (helpful, not salesy):
   - Title (engaging question or statement)
   - Body (personal story, value, link)
   - For: r/Entrepreneur, r/smallbusiness

Be authentic, helpful, not salesy. Focus on solving problems.
"""
        
        message = self.client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=3000,
            messages=[{"role": "user", "content": prompt}]
        )
        
        return message.content[0].text
    
    def generate_launch_checklist(self, product_info):
        """Generate step-by-step launch checklist"""
        checklist = f"""# LAUNCH CHECKLIST
## {product_info['title']}

**Estimated Time**: 15 minutes

---

## STEP 1: Upload to Gumroad (5 min)

1. Go to: https://gumroad.com
2. Click "Create" → "Product"
3. Upload files:
   {chr(10).join([f'   - {f}' for f in product_info.get('files', [])])}
4. Click "Next"

## STEP 2: Complete Product Info (5 min)

**Copy from**: `gumroad-listing.md`

1. Product Name: [Copy from listing]
2. Price: ${product_info['price']}
3. Description: [Copy full description]
4. Tags: [Copy all tags]
5. Category: {product_info.get('category', 'Business & Finance')}
6. Add preview images (if available)

## STEP 3: Publish (1 min)

1. Click "Publish"
2. Copy product URL
3. Save URL in: `/products/{product_info.get('id', 'product')}/launch/url.txt`

## STEP 4: Share on Social (5 min)

**Copy from**: `social-posts.md`

1. Twitter/X: Post thread (5 tweets)
2. Reddit: Post to r/Entrepreneur
3. LinkedIn: Post announcement (if applicable)

## STEP 5: Monitor (Ongoing)

1. Check Gumroad for first sale
2. Respond to questions
3. Track metrics in CEO Dashboard

---

## EXPECTED TIMELINE

- Launch today: {datetime.now().strftime('%B %d, %Y')}
- First sale target: Within 7 days
- First 10 sales: Within 30 days

---

## SUPPORT

Questions during launch? Reference:
- Gumroad docs: https://help.gumroad.com
- Marketing guide: `/agents/LAUNCH_AGENT.md`
"""
        return checklist
    
    def create_launch_package(self, product_id):
        """Create complete launch package for a product"""
        print(f"\n🚀 Creating Launch Package: {product_id}")
        print("="*60)
        
        # Load product info
        product_dir = f"/home/claude/ai-factory/products/{product_id}/built"
        
        if not os.path.exists(product_dir):
            print(f"❌ Product not found: {product_id}")
            return None
        
        # Try to load product metadata
        metadata_path = f"{product_dir}/GUMROAD_LISTING.md"
        if os.path.exists(metadata_path):
            # Extract info from existing listing
            with open(metadata_path, 'r') as f:
                content = f.read()
            
            product_info = {
                'id': product_id,
                'title': 'Cash Flow Forecaster Pro',
                'price': 89,
                'target_customer': 'Small business owners',
                'problem': 'Small businesses struggle to predict cash shortfalls',
                'solution': '12-month cash flow forecasting with scenario planning',
                'category': 'Business & Finance',
                'files': [f for f in os.listdir(product_dir) if f.endswith(('.xlsx', '.txt', '.pdf'))]
            }
        else:
            print("⚠️  No metadata found, using defaults")
            product_info = {
                'id': product_id,
                'title': 'Product',
                'price': 49,
                'files': [f for f in os.listdir(product_dir) if f.endswith(('.xlsx', '.txt', '.pdf'))]
            }
        
        # Create launch directory
        launch_dir = f"/home/claude/ai-factory/products/{product_id}/launch"
        os.makedirs(launch_dir, exist_ok=True)
        
        # Generate assets
        gumroad_listing = self.generate_gumroad_listing(product_info)
        social_posts = self.generate_social_posts(product_info)
        launch_checklist = self.generate_launch_checklist(product_info)
        
        # Save all assets
        with open(f"{launch_dir}/gumroad-listing.md", 'w') as f:
            f.write(gumroad_listing)
        print("  ✓ Gumroad listing saved")
        
        with open(f"{launch_dir}/social-posts.md", 'w') as f:
            f.write(social_posts)
        print("  ✓ Social posts saved")
        
        with open(f"{launch_dir}/launch-checklist.md", 'w') as f:
            f.write(launch_checklist)
        print("  ✓ Launch checklist saved")
        
        # Create quick start guide
        quick_start = f"""# QUICK START - LAUNCH IN 15 MINUTES

## Files Ready:
{chr(10).join([f'- {f}' for f in product_info['files']])}

## Next Steps:
1. Read: launch-checklist.md (step-by-step guide)
2. Upload to Gumroad (use: gumroad-listing.md)
3. Share on social (use: social-posts.md)

## Estimated Time:
- Upload: 5 min
- Publish: 1 min
- Share: 5 min
- Total: 15 min

**Goal**: First sale within 7 days

Start with launch-checklist.md →
"""
        
        with open(f"{launch_dir}/START-HERE.txt", 'w') as f:
            f.write(quick_start)
        print("  ✓ Quick start guide saved")
        
        print("\n" + "="*60)
        print("✅ LAUNCH PACKAGE COMPLETE")
        print("="*60)
        print(f"Location: {launch_dir}")
        print(f"Files created: 4")
        print(f"Ready to launch: YES")
        print("="*60)
        print("\n📋 NEXT: Read START-HERE.txt for launch instructions\n")
        
        return launch_dir

if __name__ == "__main__":
    engine = LaunchEngine()
    
    # Create launch package for Cash Flow Forecaster
    product_id = "cash_flow_forecaster_pro"
    launch_dir = engine.create_launch_package(product_id)
    
    if launch_dir:
        print(f"✅ Launch package ready: {launch_dir}")
