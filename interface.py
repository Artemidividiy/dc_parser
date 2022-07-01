import streamlit as st
import parser
from streamlit_echarts import st_echarts
class Interface:
    def __init__(self) -> None:
        self.table_of_restaurant = parser.Parser().get_items()
    def calc_uses_delivery(self):
        
        yes = len(list(filter(lambda x: x.uses_delivery == "yes", self.table_of_restaurant)))
        no = len(list(filter(lambda x: x.uses_delivery == "no", self.table_of_restaurant)))
        return yes, no
    def run(self):
        st.header("Доставки ресторанов")
        st.dataframe(self.table_of_restaurant)
        pie_uses_delivery = self.calc_uses_delivery()
        options = {
            "tooltip": {"trigger": "item"},
            "legend": {"top": "5%", "left": "center"},
            "series": [
                {
                    "name": "own and dc delivery service comparison",
                    "type": "pie",
                    "radius": ["40%", "70%"],
                    "avoidLabelOverlap": False,
                    "itemStyle": {
                        "borderRadius": 10,
                        "borderColor": "#fff",
                        "borderWidth": 2,
                    },
                    "label": {"show": False, "position": "center"},
                    "emphasis": {
                        "label": {"show": True, "fontSize": "40", "fontWeight": "bold"}
                    },
                    "labelLine": {"show": False},
                    "data": [
                        {"value": pie_uses_delivery[0], "name": "yes"},
                        {"value": pie_uses_delivery[1], "name": "no"},
                    ],
                }
            ],
        }
        st_echarts(
            options=options, height="500px",
        )

if __name__ == "__main__":
    Interface().run()