import pandas as pd
import plotly.express as px

from dash import Dash, dcc, html, Input, Output


# =========================================================
# Load Data
# =========================================================

df = pd.read_csv("C:/Users/hp/Desktop/CA-S2-G1-AI/CA_AIS2_G1_Ml/src/data_analysis/dash/Dash.csv")


# Get numerical columns
num_cols = df.select_dtypes(include="number").columns


# =========================================================
# Create Dash App
# =========================================================

app = Dash(__name__)
app.title = "Interactive Data Dashboard"


# =========================================================
# Colors
# =========================================================

BACKGROUND = "#f5f7fb"
CARD_BACKGROUND = "white"
TEXT = "#1f2937"
SECONDARY_TEXT = "#6b7280"
PRIMARY = "#2563eb"


# =========================================================
# Layout
# =========================================================

app.layout = html.Div(

    [

        # -------------------------------------------------
        # Header
        # -------------------------------------------------

        html.Div(

            [

                html.H1(
                    "Interactive Data Dashboard",
                    style={
                        "margin": "0",
                        "fontSize": "32px",
                        "fontWeight": "700"
                    }
                ),

                html.P(
                    "Explore and compare numerical data by Area",
                    style={
                        "marginTop": "8px",
                        "color": SECONDARY_TEXT,
                        "fontSize": "16px"
                    }
                )

            ],

            style={
                "padding": "30px 40px",
                "backgroundColor": CARD_BACKGROUND,
                "borderBottom": "1px solid #e5e7eb"
            }
        ),


        # -------------------------------------------------
        # Main Content
        # -------------------------------------------------

        html.Div(

            [

                # -----------------------------------------
                # Column Selector
                # -----------------------------------------

                html.Div(

                    [

                        html.Label(
                            "Select Metric",
                            style={
                                "fontWeight": "600",
                                "fontSize": "15px",
                                "marginBottom": "8px",
                                "display": "block"
                            }
                        ),

                        dcc.Dropdown(
                            id="column-dropdown",

                            options=[
                                {
                                    "label": col.replace("_", " ").title(),
                                    "value": col
                                }
                                for col in num_cols
                            ],

                            value=num_cols[0],

                            clearable=False,

                            style={
                                "width": "100%"
                            }
                        )

                    ],

                    style={
                        "backgroundColor": CARD_BACKGROUND,
                        "padding": "20px",
                        "borderRadius": "12px",
                        "marginBottom": "25px",
                        "boxShadow": "0 2px 8px rgba(0,0,0,0.05)"
                    }
                ),


                # -----------------------------------------
                # KPI Cards
                # -----------------------------------------

                html.Div(

                    [

                        html.Div(
                            [
                                html.P(
                                    "Number of Areas",
                                    style={
                                        "color": SECONDARY_TEXT,
                                        "margin": "0"
                                    }
                                ),

                                html.H2(
                                    id="areas-kpi",
                                    style={
                                        "margin": "8px 0 0",
                                        "color": TEXT
                                    }
                                )
                            ],
                            className="kpi-card"
                        ),


                        html.Div(
                            [
                                html.P(
                                    "Total Value",
                                    style={
                                        "color": SECONDARY_TEXT,
                                        "margin": "0"
                                    }
                                ),

                                html.H2(
                                    id="total-kpi",
                                    style={
                                        "margin": "8px 0 0",
                                        "color": TEXT
                                    }
                                )
                            ],
                            className="kpi-card"
                        ),


                        html.Div(
                            [
                                html.P(
                                    "Average Value",
                                    style={
                                        "color": SECONDARY_TEXT,
                                        "margin": "0"
                                    }
                                ),

                                html.H2(
                                    id="average-kpi",
                                    style={
                                        "margin": "8px 0 0",
                                        "color": TEXT
                                    }
                                )
                            ],
                            className="kpi-card"
                        ),


                        html.Div(
                            [
                                html.P(
                                    "Top Area",
                                    style={
                                        "color": SECONDARY_TEXT,
                                        "margin": "0"
                                    }
                                ),

                                html.H2(
                                    id="top-area-kpi",
                                    style={
                                        "margin": "8px 0 0",
                                        "color": TEXT,
                                        "fontSize": "22px"
                                    }
                                )
                            ],
                            className="kpi-card"
                        )

                    ],

                    style={
                        "display": "grid",
                        "gridTemplateColumns":
                            "repeat(4, 1fr)",
                        "gap": "20px",
                        "marginBottom": "25px"
                    }
                ),


                # -----------------------------------------
                # Charts
                # -----------------------------------------

                html.Div(

                    [

                        # Pie Chart

                        html.Div(

                            [

                                dcc.Graph(
                                    id="pie-chart",
                                    config={
                                        "displayModeBar": False
                                    }
                                )

                            ],

                            style={
                                "backgroundColor": CARD_BACKGROUND,
                                "borderRadius": "12px",
                                "padding": "10px",
                                "boxShadow":
                                    "0 2px 8px rgba(0,0,0,0.05)"
                            }
                        ),


                        # Bar Chart

                        html.Div(

                            [

                                dcc.Graph(
                                    id="bar-chart",
                                    config={
                                        "displayModeBar": False
                                    }
                                )

                            ],

                            style={
                                "backgroundColor": CARD_BACKGROUND,
                                "borderRadius": "12px",
                                "padding": "10px",
                                "boxShadow":
                                    "0 2px 8px rgba(0,0,0,0.05)"
                            }
                        )

                    ],

                    style={
                        "display": "grid",
                        "gridTemplateColumns":
                            "1fr 1fr",
                        "gap": "25px",
                        "marginBottom": "25px"
                    }
                ),


                # -----------------------------------------
                # Data Table
                # -----------------------------------------

                html.Div(

                    [

                        html.H3(
                            "Area Summary",
                            style={
                                "marginTop": "0",
                                "color": TEXT
                            }
                        ),

                        html.Div(
                            id="summary-table"
                        )

                    ],

                    style={
                        "backgroundColor": CARD_BACKGROUND,
                        "borderRadius": "12px",
                        "padding": "25px",
                        "boxShadow":
                            "0 2px 8px rgba(0,0,0,0.05)"
                    }
                )

            ],

            style={
                "padding": "30px 40px"
            }
        )

    ],

    style={
        "backgroundColor": BACKGROUND,
        "minHeight": "100vh",
        "fontFamily": "Arial, sans-serif"
    }
)


# =========================================================
# Callback
# =========================================================

@app.callback(

    [
        Output("pie-chart", "figure"),
        Output("bar-chart", "figure"),
        Output("areas-kpi", "children"),
        Output("total-kpi", "children"),
        Output("average-kpi", "children"),
        Output("top-area-kpi", "children"),
        Output("summary-table", "children")
    ],

    Input("column-dropdown", "value")
)


def update_dashboard(selected_col):

    # ---------------------------------------------
    # Group data by Area
    # ---------------------------------------------

    grouped = (
        df.groupby("Area")[selected_col]
        .sum()
        .reset_index()
        .sort_values(selected_col, ascending=False)
    )


    # ---------------------------------------------
    # KPI calculations
    # ---------------------------------------------

    number_of_areas = grouped["Area"].nunique()

    total_value = grouped[selected_col].sum()

    average_value = grouped[selected_col].mean()

    top_area = grouped.iloc[0]["Area"]


    # ---------------------------------------------
    # Pie Chart
    # ---------------------------------------------

    fig_pie = px.pie(

        grouped,

        names="Area",

        values=selected_col,

        title=f"Distribution of {selected_col.replace('_', ' ').title()} by Area",

        hole=0.45

    )

    fig_pie.update_traces(
        textposition="inside",
        textinfo="percent+label"
    )

    fig_pie.update_layout(
        margin=dict(t=70, l=20, r=20, b=20),
        legend_title="Area"
    )


    # ---------------------------------------------
    # Bar Chart
    # ---------------------------------------------

    fig_bar = px.bar(

        grouped,

        x="Area",

        y=selected_col,

        title=f"{selected_col.replace('_', ' ').title()} by Area",

        text_auto=".2s"

    )

    fig_bar.update_layout(
        xaxis_title="Area",
        yaxis_title=selected_col.replace("_", " ").title(),
        margin=dict(t=70, l=20, r=20, b=20)
    )


    # ---------------------------------------------
    # Summary Table
    # ---------------------------------------------

    table_header = html.Tr(

        [

            html.Th(
                "Area",
                style={"padding": "12px"}
            ),

            html.Th(
                selected_col.replace("_", " ").title(),
                style={"padding": "12px"}
            )

        ]

    )


    table_rows = []

    for _, row in grouped.iterrows():

        table_rows.append(

            html.Tr(

                [

                    html.Td(
                        row["Area"],
                        style={"padding": "10px"}
                    ),

                    html.Td(
                        f"{row[selected_col]:,.2f}",
                        style={"padding": "10px"}
                    )

                ]

            )

        )


    table = html.Table(

        [

            html.Thead(table_header),

            html.Tbody(table_rows)

        ],

        style={
            "width": "100%",
            "borderCollapse": "collapse",
            "textAlign": "left"
        }

    )


    return (

        fig_pie,

        fig_bar,

        f"{number_of_areas:,}",

        f"{total_value:,.2f}",

        f"{average_value:,.2f}",

        str(top_area),

        table

    )


# =========================================================
# Run App
# =========================================================

if __name__ == "__main__":
    app.run(debug=True)