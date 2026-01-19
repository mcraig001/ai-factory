# DISCOVERY AGENT
## Autonomous Opportunity Research & Validation System

---

## MISSION
Continuously discover, research, and validate sellable product opportunities without human intervention. Present only high-quality, data-backed opportunities to CEO for approval.

---

## CORE PHILOSOPHY

**NOT**: "What can AI build easily?"  
**YES**: "What do customers desperately need and will pay for?"

**Validation Hierarchy**:
1. **Proven demand** (people already buying similar products)
2. **Clear pain point** (frustration expressed publicly)
3. **Willingness to pay** (price points established)
4. **Competitive gaps** (opportunity to do it better)

---

## DATA SOURCES (Priority Order)

### **Tier 1: Marketplaces** (What's SELLING)
1. **Gumroad**:
   - Top products in "Productivity" and "Business"
   - Sort by "Popular" 
   - Extract: Title, price, description, sales indicators
   - Look for: Templates, spreadsheets, tools, dashboards

2. **Creative Market**:
   - Excel templates section
   - Notion templates
   - Business tools
   - Extract: Best sellers, prices, reviews

3. **Etsy** (Digital Downloads):
   - Business & Finance section
   - Spreadsheets & tools
   - Extract: Sales count, reviews, pricing

### **Tier 2: Communities** (What People NEED)
1. **Reddit**:
   - r/Entrepreneur (pain points, tool requests)
   - r/SideHustle (what people are building)
   - r/smallbusiness (operational needs)
   - r/freelance (freelancer pain points)
   - r/RealEstateInvesting (investor tools)
   - Search terms: "need a template", "looking for spreadsheet", "wish there was a tool"

2. **Twitter/X**:
   - Search: "need a template for"
   - Search: "looking for excel"
   - Monitor: @IndieHackers, @levelsio, @gregisenberg for trends

3. **Indie Hackers**:
   - Product ideas section
   - Revenue milestones (what's working)

### **Tier 3: Competitive Analysis**
1. **Product Hunt**:
   - Productivity tools launches
   - What gets upvotes
   - Comment analysis

2. **MicroAcquire / Flippa**:
   - What businesses are selling for
   - Valuation multiples
   - Proven business models

---

## OPPORTUNITY SCORING SYSTEM

**Each opportunity scored 0-100 based on**:

### **Market Demand** (40 points)
- Existing products selling (10 pts)
- High prices sustained ($50+) (10 pts)
- Multiple competitors (validation) (10 pts)
- Reddit/community requests (10 pts)

### **Revenue Potential** (30 points)
- Price point $50-150 (15 pts)
- High volume potential (15 pts)

### **Competitive Advantage** (20 points)
- Clear gap in existing solutions (10 pts)
- Can be built better with AI (10 pts)

### **Speed to Market** (10 points)
- Can ship in 1-3 days (10 pts)
- Simple enough to automate (5 pts)
- No complex integrations needed (5 pts)

**Threshold**: Only opportunities scoring 70+ are presented to CEO

---

## DISCOVERY WORKFLOW

### **Phase 1: Data Collection** (Automated)

**Gumroad Scraping**:
```
1. Navigate to gumroad.com/discover
2. Filter: Digital Products → Productivity
3. Sort: Most Popular
4. Extract top 50 products:
   - Title
   - Price
   - Description
   - Category
   - Sales indicators (followers, ratings)
```

**Reddit Scraping**:
```
1. Search r/Entrepreneur: "need a template" (last 30 days)
2. Search r/smallbusiness: "looking for spreadsheet"
3. Search r/freelance: "wish there was"
4. Extract:
   - Post title
   - Upvotes
   - Comment count
   - Top solutions suggested
   - Unmet needs
```

### **Phase 2: Pattern Analysis** (Claude AI)

**Input**: Raw scraped data  
**Process**: Claude analyzes for:
- Common pain points
- Price clustering
- Feature requests
- Competitive gaps
- Unmet needs

**Output**: Categorized opportunities with evidence

### **Phase 3: Opportunity Generation**

For each identified opportunity:

**Create Brief**:
```json
{
  "opportunity_id": "unique_id",
  "title": "Clear, specific name",
  "category": "Real Estate / Freelance / E-commerce / etc",
  "problem": "Specific pain point (1-2 sentences)",
  "solution": "What we'll build",
  "target_customer": "Who needs this",
  "price_point": "$XX (based on market)",
  "evidence": {
    "gumroad_examples": ["Product A ($XX)", "Product B ($XX)"],
    "reddit_posts": ["Link to post with 150 upvotes"],
    "existing_demand": "X products selling at $XX"
  },
  "competitive_gap": "Why we can do it better",
  "revenue_projection": {
    "price": XX,
    "monthly_sales_target": XX,
    "monthly_revenue": XX
  },
  "build_time": "X days",
  "score": XX,
  "score_breakdown": {
    "market_demand": XX,
    "revenue_potential": XX,
    "competitive_advantage": XX,
    "speed_to_market": XX
  },
  "recommendation": "BUILD / TEST / PASS"
}
```

### **Phase 4: CEO Presentation**

**Dashboard shows**:
- Top 10 opportunities (sorted by score)
- Evidence for each
- One-click approve/reject
- Auto-proceeds to building if approved

---

## VALIDATION RULES

**NEVER present opportunities that**:
- Score below 70/100
- Have no proven market (zero existing products)
- Price below $25 (not worth the effort)
- Require ongoing support/service
- Need complex integrations
- Can't be automated

**ALWAYS prefer opportunities that**:
- Have 3+ existing products selling
- Show Reddit posts with 50+ upvotes asking for solution
- Price point $50-150
- Can be built in 1-3 days
- Fit template/spreadsheet/tool format

---

## EXAMPLE OPPORTUNITIES (Format)

### **Opportunity #1: Real Estate Deal Analyzer**
- **Score**: 87/100
- **Problem**: Real estate investors spend hours analyzing deals manually
- **Solution**: Excel template with BRRRR, flip, rental ROI calculations
- **Evidence**:
  - Gumroad: 5 similar products at $79-149
  - Reddit: 12 posts in r/RealEstateInvesting asking for this
  - Existing market: $XX,XXX/month (estimated)
- **Price**: $99
- **Build time**: 2 days
- **Recommendation**: BUILD

### **Opportunity #2: Freelance Profit Tracker**
- **Score**: 82/100
- **Problem**: Freelancers don't know which clients are profitable
- **Solution**: Time tracking + project profitability dashboard
- **Evidence**:
  - Gumroad: 8 products at $39-69
  - Reddit: r/freelance posts weekly asking for this
- **Price**: $49
- **Build time**: 1 day
- **Recommendation**: BUILD

---

## AUTOMATION SCHEDULE

**Daily** (runs automatically):
- Scan Gumroad new popular products
- Scan Reddit for new pain points
- Update opportunity scores

**Weekly**:
- Deep analysis of trends
- Competitive landscape update
- Price point adjustments

**Monthly**:
- Strategic review with CEO
- Market shift analysis
- New category exploration

---

## SUCCESS METRICS

**Discovery Performance**:
- Opportunities generated per week: 5-10
- Opportunities scoring 70+: 3-5
- Opportunities approved by CEO: 1-2
- Approved opportunities that launch: 100%
- Launched products that make first sale: 80%+

**Quality Indicators**:
- Average opportunity score: >75
- Evidence strength (sources per opportunity): 3+
- Price accuracy (within 10% of market): 90%+

---

## CONTINUOUS IMPROVEMENT

**Learn from**:
- Which opportunities CEO approves (pattern recognition)
- Which products actually sell (validate scoring)
- Customer feedback (refine understanding)

**Adapt**:
- Scoring weights based on what sells
- New data sources (if patterns emerge)
- Category focus (double down on winners)

---

## OUTPUT FORMAT

**For CEO Dashboard**:
```json
{
  "discovery_run_id": "timestamp",
  "opportunities": [
    {opportunity_object},
    {opportunity_object}
  ],
  "metadata": {
    "sources_scraped": 5,
    "total_data_points": 500,
    "opportunities_found": 25,
    "opportunities_above_threshold": 8,
    "top_categories": ["Real Estate", "Freelance", "E-commerce"],
    "avg_price_point": "$XX",
    "recommended_next_build": "opportunity_id"
  }
}
```

---

## NEXT ACTIONS (CEO APPROVAL REQUIRED)

1. [ ] Approve this discovery strategy
2. [ ] Run first discovery sweep
3. [ ] Review top 10 opportunities
4. [ ] Approve 1-2 for immediate building

**Once approved, Discovery Agent runs autonomously and presents only validated opportunities.**
