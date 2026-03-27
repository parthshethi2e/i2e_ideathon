 🚀 AI Lead Generator for Pharma & PPM

### 🔄 Pipeline Flow

1. **User Input**

   * i2e Offering (e.g., CTMS, PPM)
   * Location (optional)

2. **AI Persona Generation**

   * Uses OpenAI/OpenRouter
   * Outputs:

     * Target job titles
     * Relevant keywords

3. **Query Builder**

   * Constructs optimized Google/LinkedIn queries

4. **Search Layer**

   * Uses SerpAPI to fetch real search results

5. **Lead Extraction**

   * Parses:

     * Name
     * Role
     * Company
     * Source

6. **Lead Scoring Engine**

   * Scores based on:

     * Role seniority (CEO, CTO, VP)
     * Keyword relevance
     * Domain alignment

7. **Ranking & Output**

   * Displays:

     * Ranked leads
     * Persona tables
     * KPI insights

---

## 🏗️ Tech Stack

| Layer           | Technology          |
| --------------- | ------------------- |
| Frontend        | Shiny (Python)      |
| Backend         | Python              |
| AI              | OpenAI / OpenRouter |
| Search          | SerpAPI             |
| Data Processing | Pandas              |
| Deployment      | Render              |

---

## 📂 Project Structure

```
i2e_shiny/
│
├── app.py                     # Shiny UI
│
├── pipeline/
│   └── run_pipeline.py       # Main pipeline orchestration
│
├── ai/
│   └── persona_extractor.py  # AI persona generation
│
├── scraper/
│   └── search.py             # SerpAPI integration
│
├── utils/
│   ├── parser.py             # Lead extraction
│   └── helpers.py
│
├── scorer/
│   └── lead_scorer.py        # Scoring logic
│
├── requirements.txt
├── render.yaml
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone <your-repo-url>
cd i2e_shiny
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv i2e_env
source i2e_env/bin/activate   # Mac/Linux
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Set Environment Variables

```bash
export OPENAI_API_KEY=your_openrouter_key
export SERP_API_KEY=your_serpapi_key
```

---

### 5️⃣ Run Locally

```bash
shiny run app.py
```

---

## 🌐 Deployment (Render)

1. Push code to GitHub
2. Go to Render → New Web Service
3. Use:

```bash
Build Command: pip install -r requirements.txt
Start Command: shiny run app.py --host 0.0.0.0 --port 10000
```

4. Add environment variables:

   * OPENAI_API_KEY
   * SERP_API_KEY

---

## 📊 Scoring Methodology

Each lead is scored based on **verifiable signals**:

| Signal             | Description                 |
| ------------------ | --------------------------- |
| Role Seniority     | CEO, CTO, VP > Manager      |
| Domain Match       | Pharma / Clinical relevance |
| Keyword Match      | Alignment with offering     |
| Source Credibility | LinkedIn profiles           |

---

## 📈 Sample Output

* 🎯 Persona (Titles & Keywords)
* 🔍 Search Query
* 🏆 Ranked Leads
* 🔥 High-Intent Prospects

---

## 🚀 Key Features

* AI-driven persona discovery
* Real-time web data extraction
* Explainable lead scoring
* Scalable pipeline architecture
* Deployable production system

---

## 💡 Future Enhancements

* 📊 Score visualization (charts)
* 🧠 Lead explanation panel (“Why this lead?”)
* 🔔 Hiring signal detection (job postings)
* 📬 CRM integration (HubSpot, Salesforce)
* 🤖 Autonomous AI agents

---

## 🏁 Conclusion

This system demonstrates how AI + real-time web data can:

👉 Turn the internet into a **qualified B2B pipeline**
👉 Identify **decision-makers with precision**
👉 Reduce manual effort in lead generation

---

## 👨‍💻 Author

**Parth Sheth**
Senior Software Developer – Mobile
AI & Life Sciences Enthusiast

