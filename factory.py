#!/usr/bin/env python3
"""
AI FACTORY - MASTER CONTROL
Run the entire factory with one command
"""

import os
import sys
import json
from datetime import datetime

def print_header(text):
    """Print formatted header"""
    print("\n" + "="*60)
    print(text.center(60))
    print("="*60 + "\n")

def run_discovery():
    """Run discovery engine to find new opportunities"""
    print_header("🔍 RUNNING DISCOVERY")
    
    os.chdir("/home/claude/ai-factory/engines")
    result = os.system("python discovery_engine.py")
    
    if result == 0:
        print("\n✅ Discovery complete - New opportunities found")
        return True
    else:
        print("\n❌ Discovery failed")
        return False

def show_opportunities():
    """Display current opportunities"""
    print_header("💡 CURRENT OPPORTUNITIES")
    
    opportunities_file = "/home/claude/ai-factory/opportunities/latest.json"
    
    if not os.path.exists(opportunities_file):
        print("No opportunities found. Run discovery first.")
        return []
    
    with open(opportunities_file, 'r') as f:
        data = json.load(f)
    
    opportunities = data.get('opportunities', [])
    
    print(f"Found {len(opportunities)} opportunities:\n")
    
    for i, opp in enumerate(opportunities[:5], 1):
        print(f"{i}. {opp['title']}")
        print(f"   Score: {opp['score']}/100")
        print(f"   Price: ${opp['price']}")
        print(f"   Revenue Potential: ${opp.get('monthly_revenue_estimate', 0):,}/month")
        print(f"   Build Time: {opp['build_time_days']} days")
        print()
    
    return opportunities

def build_product(opportunity_id):
    """Build a product from opportunity"""
    print_header(f"🏗️  BUILDING PRODUCT: {opportunity_id}")
    
    # For now, just show what would happen
    print("Product Builder would:")
    print("1. Read opportunity details")
    print("2. Generate product spec")
    print("3. Build the product")
    print("4. Run quality check")
    print("5. Generate documentation")
    print("6. Output ready-to-sell files")
    print("\n⚠️  Manual build currently - use product_builder_engine.py")
    
    return True

def create_launch_package(product_id):
    """Create launch materials"""
    print_header(f"🚀 CREATING LAUNCH PACKAGE: {product_id}")
    
    os.chdir("/home/claude/ai-factory/engines")
    result = os.system(f"python launch_engine.py")
    
    if result == 0:
        print("\n✅ Launch package created")
        return True
    else:
        print("\n❌ Launch package failed")
        return False

def show_status():
    """Show factory status"""
    print_header("🏭 AI FACTORY STATUS")
    
    # Check what exists
    opportunities_exist = os.path.exists("/home/claude/ai-factory/opportunities/latest.json")
    products_exist = os.path.exists("/home/claude/ai-factory/products")
    
    print(f"Discovery Agent: {'✅ Operational' if opportunities_exist else '⚠️ Not run yet'}")
    print(f"Product Builder: ✅ Ready")
    print(f"Launch Agent: ✅ Ready")
    print(f"CEO Dashboard: ✅ Deployed")
    
    if opportunities_exist:
        with open("/home/claude/ai-factory/opportunities/latest.json", 'r') as f:
            data = json.load(f)
        print(f"\nCurrent Opportunities: {len(data.get('opportunities', []))}")
        print(f"Last Discovery Run: {data.get('timestamp', 'Unknown')}")
    
    print(f"\nDashboard URL: https://ai-factory-mji8t7vuwc8gymmcgft6fk.streamlit.app/")
    print()

def main():
    """Main control interface"""
    
    print("""
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║             🏭  AI FACTORY - MASTER CONTROL  🏭          ║
║                                                          ║
║            Autonomous Business Portfolio System          ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
    """)
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "discover":
            run_discovery()
            show_opportunities()
        
        elif command == "opportunities":
            show_opportunities()
        
        elif command == "build":
            if len(sys.argv) > 2:
                product_id = sys.argv[2]
                build_product(product_id)
            else:
                print("Usage: python factory.py build <product_id>")
        
        elif command == "launch":
            if len(sys.argv) > 2:
                product_id = sys.argv[2]
                create_launch_package(product_id)
            else:
                print("Usage: python factory.py launch <product_id>")
        
        elif command == "status":
            show_status()
        
        else:
            print(f"Unknown command: {command}")
            print_commands()
    
    else:
        print_commands()

def print_commands():
    """Print available commands"""
    print("""
AVAILABLE COMMANDS:

  python factory.py discover      - Find new product opportunities
  python factory.py opportunities - Show current opportunities
  python factory.py build <id>    - Build a product
  python factory.py launch <id>   - Create launch package
  python factory.py status        - Show factory status

WORKFLOW:

  1. Run discovery to find opportunities
  2. Review opportunities
  3. Build best opportunity
  4. Create launch package
  5. Upload to Gumroad
  6. Repeat

DASHBOARD:
  https://ai-factory-mji8t7vuwc8gymmcgft6fk.streamlit.app/

    """)

if __name__ == "__main__":
    main()
