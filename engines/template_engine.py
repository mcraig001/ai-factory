"""
Template Builder Engine
Reads TEMPLATE_BUILDER_AGENT.md and executes the template creation workflow
"""

import os
import json
import anthropic
from datetime import datetime

# Initialize Anthropic client
import os
client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY")
)

class TemplateBuilder:
    def __init__(self):
        self.agent_instructions = self.load_agent_instructions()
        self.templates_created = []
        
    def load_agent_instructions(self):
        """Load the TEMPLATE_BUILDER_AGENT.md file"""
        agent_path = "/home/claude/ai-factory/agents/TEMPLATE_BUILDER_AGENT.md"
        with open(agent_path, 'r') as f:
            return f.read()
    
    def generate_template_concept(self, category="Financial Dashboards"):
        """Use Claude to generate a template concept based on agent instructions"""
        
        prompt = f"""Based on these instructions:

{self.agent_instructions}

Generate a detailed template concept for category: {category}

Return a JSON object with:
{{
    "name": "Template name",
    "description": "What it does",
    "target_audience": "Who needs this",
    "key_features": ["feature1", "feature2", "feature3"],
    "price_point": "$XX",
    "quality_score_prediction": "XX/100",
    "design_specs": {{
        "color_scheme": ["color1", "color2"],
        "layout": "description",
        "key_sections": ["section1", "section2"]
    }},
    "example_use_case": "Real-world scenario"
}}

Focus on high-demand templates that will sell well."""

        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=2000,
            messages=[{"role": "user", "content": prompt}]
        )
        
        # Extract JSON from response
        response_text = message.content[0].text
        
        # Find JSON in response (handle markdown code blocks)
        if "```json" in response_text:
            json_text = response_text.split("```json")[1].split("```")[0].strip()
        elif "```" in response_text:
            json_text = response_text.split("```")[1].split("```")[0].strip()
        else:
            json_text = response_text.strip()
        
        return json.loads(json_text)
    
    def create_template_structure(self, concept):
        """Generate the actual template structure (simplified for MVP)"""
        
        prompt = f"""Create a professional financial template structure for:

{json.dumps(concept, indent=2)}

Design requirements from agent:
- Clean, professional corporate aesthetic
- No AI slop (purple gradients, generic icons)
- Professional color palette
- Grid-based layout

Generate the structure as a detailed specification that includes:
1. Sheet/tab names
2. Section layouts
3. Formula descriptions
4. Color coding system
5. Example data structure

Return as structured text (not actual Excel, we'll build that next)."""

        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=4000,
            messages=[{"role": "user", "content": prompt}]
        )
        
        return message.content[0].text
    
    def quality_check(self, concept, structure):
        """Score the template against quality checklist"""
        
        prompt = f"""Score this template concept and structure against the quality checklist:

CONCEPT:
{json.dumps(concept, indent=2)}

STRUCTURE:
{structure}

QUALITY CHECKLIST (from agent):
- Design Quality (40 points): Professional colors, typography, layout, no AI slop
- Functionality (30 points): Formulas work, easy to customize, no errors
- Completeness (30 points): Instructions, examples, variations

Return JSON:
{{
    "total_score": "XX/100",
    "design_score": "XX/40",
    "functionality_score": "XX/30", 
    "completeness_score": "XX/30",
    "passes_threshold": true/false,
    "feedback": "What's good and what needs improvement"
}}

Threshold is 85/100 to pass."""

        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1500,
            messages=[{"role": "user", "content": prompt}]
        )
        
        response_text = message.content[0].text
        if "```json" in response_text:
            json_text = response_text.split("```json")[1].split("```")[0].strip()
        else:
            json_text = response_text.strip()
        
        return json.loads(json_text)
    
    def generate_template_package(self, concept, structure, quality_score):
        """Create the submission package for CEO approval"""
        
        package = {
            "id": f"template_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            "created_at": datetime.now().isoformat(),
            "status": "pending_approval",
            "concept": concept,
            "structure": structure,
            "quality_score": quality_score,
            "recommendation": "APPROVE" if quality_score.get("passes_threshold") else "REVISE"
        }
        
        # Save to file for CEO Dashboard to read
        output_dir = "/home/claude/ai-factory/products/financial-templates/pending"
        os.makedirs(output_dir, exist_ok=True)
        
        output_path = f"{output_dir}/{package['id']}.json"
        with open(output_path, 'w') as f:
            json.dump(package, f, indent=2)
        
        print(f"\n✓ Template package created: {package['id']}")
        print(f"  Quality Score: {quality_score['total_score']}")
        print(f"  Recommendation: {package['recommendation']}")
        print(f"  Saved to: {output_path}")
        
        return package
    
    def run_template_creation(self, count=3):
        """Main workflow: Create specified number of templates"""
        
        print(f"\n{'='*60}")
        print(f"TEMPLATE BUILDER ENGINE - Creating {count} templates")
        print(f"{'='*60}\n")
        
        categories = [
            "Financial Dashboards",
            "Forecasting & Planning", 
            "Pitch & Reporting"
        ]
        
        results = []
        
        for i in range(count):
            category = categories[i % len(categories)]
            
            print(f"\n[{i+1}/{count}] Creating template in category: {category}")
            print("-" * 60)
            
            # Step 1: Generate concept
            print("  → Generating concept...")
            concept = self.generate_template_concept(category)
            print(f"  ✓ Concept: {concept['name']}")
            
            # Step 2: Create structure
            print("  → Creating structure...")
            structure = self.create_template_structure(concept)
            print(f"  ✓ Structure created ({len(structure)} characters)")
            
            # Step 3: Quality check
            print("  → Running quality check...")
            quality_score = self.quality_check(concept, structure)
            print(f"  ✓ Quality Score: {quality_score['total_score']}")
            
            # Step 4: Package for approval
            print("  → Packaging for CEO approval...")
            package = self.generate_template_package(concept, structure, quality_score)
            
            results.append(package)
            print(f"\n  {'✓ READY FOR APPROVAL' if quality_score.get('passes_threshold') else '⚠ NEEDS REVISION'}")
        
        print(f"\n{'='*60}")
        print(f"SUMMARY: {count} templates created")
        print(f"  Passing quality (≥85): {sum(1 for r in results if r['recommendation'] == 'APPROVE')}")
        print(f"  Needs revision (<85): {sum(1 for r in results if r['recommendation'] == 'REVISE')}")
        print(f"\nTemplates saved to: /home/claude/ai-factory/products/financial-templates/pending/")
        print(f"CEO Dashboard will show these for approval")
        print(f"{'='*60}\n")
        
        return results

if __name__ == "__main__":
    builder = TemplateBuilder()
    results = builder.run_template_creation(count=3)
