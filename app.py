from shiny import App, ui, render, reactive
import pandas as pd
import json

from pipeline.run_pipeline import run_pipeline

# ---------------- UI ----------------
app_ui = ui.page_fluid(

    ui.div(
        ui.h2("🚀 AI Lead Generator"),
        ui.p("Find Decision Makers in Pharma & PPM"),
        class_="text-center"
    ),

    ui.hr(),

    ui.layout_sidebar(

        # ✅ Correct sidebar
        ui.sidebar(
            ui.h4("⚙️ Inputs"),

            ui.input_text(
                "offering",
                "i2e Offering",
                "Clinical Trial Management System"
            ),

            ui.input_text(
                "location",
                "Target Location",
                "United States"
            ),

            ui.input_action_button("run", "🔍 Generate Leads")
        ),

        # ✅ Main content (no panel_main)
        ui.div(

            # KPI Cards
            ui.row(
                ui.column(4,
                    ui.card(
                        ui.h5("👥 Total Leads"),
                        ui.output_text("total_leads")
                    )
                ),
                ui.column(4,
                    ui.card(
                        ui.h5("🔥 High Score Leads"),
                        ui.output_text("hot_leads")
                    )
                ),
                ui.column(4,
                    ui.card(
                        ui.h5("🏢 Unique Companies"),
                        ui.output_text("companies")
                    )
                )
            ),

            ui.hr(),

            # Persona Tables
            ui.row(
                ui.column(6,
                    ui.card(
                        ui.h4("👤 Target Titles"),
                        ui.output_table("titles_table")
                    )
                ),
                ui.column(6,
                    ui.card(
                        ui.h4("🔑 Keywords"),
                        ui.output_table("keywords_table")
                    )
                )
            ),

            ui.hr(),

            # Query
            ui.card(
                ui.h4("🎯 Search Query"),
                ui.output_text_verbatim("query")
            ),

            ui.hr(),

            # Leads Table
            ui.card(
                ui.h4("🏆 Ranked Leads"),
                ui.output_table("table")
            )
        )
    )
)

# ---------------- SERVER ----------------
def server(input, output, session):

    # Main pipeline trigger
    @reactive.event(input.run)
    def data():
        return run_pipeline(
            offering=input.offering()
        )

    # -------- KPIs --------
    @output
    @render.text
    def total_leads():
        return len(data()["leads"])

    @output
    @render.text
    def hot_leads():
        leads = data()["leads"]
        return len([l for l in leads if l["score"] >= 70])

    @output
    @render.text
    def companies():
        leads = data()["leads"]
        return len(set([l.get("company", "") for l in leads]))

    # -------- Persona Tables --------
    @output
    @render.table
    def titles_table():
        persona = data()["persona"]
        titles = persona.get("titles", [])

        return pd.DataFrame({
            "Target Titles": titles
        })

    @output
    @render.table
    def keywords_table():
        persona = data()["persona"]
        keywords = persona.get("keywords", [])

        return pd.DataFrame({
            "Keywords": keywords
        })

    # -------- Query --------
    @output
    @render.text
    def query():
        return data()["query"]

    # -------- Leads Table --------
    @output
    @render.table
    def table():
        leads = data()["leads"]

        rows = []
        for l in leads:
            rows.append({
                "Name": l.get("name", ""),
                "Role": l.get("role", ""),
                "Company": l.get("company", ""),
                "Score": l.get("score", 0),
                "Category": "🔥 Hot" if l.get("score", 0) >= 70 else "Normal"
            })

        df = pd.DataFrame(rows)

        if not df.empty:
            df = df.sort_values(by="Score", ascending=False)

        return df


# ---------------- APP ----------------
app = App(app_ui, server)