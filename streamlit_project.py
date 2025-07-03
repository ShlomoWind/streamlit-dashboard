import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#טעינת הקובץ
df = pd.read_csv("datafile.csv")
st.title("🛫Welcome to the dashboard!")
st.write("Here you can see a breakdown of flight schedule data")
st.write("Quick look at the data:")
st.dataframe(df.head())
#מחיקת עמודות עם ערכים חסרים (עמודות שאינן נחוצות לפילוח הנתונים)
df.drop(columns=['CHCKZN','CHCINT'],inplace=True)
#המרת עמודות תאריך לסוג של תאריך ושעה
df['CHPTOL'] = pd.to_datetime(df['CHPTOL'],errors='coerce')
df['CHSTOL'] = pd.to_datetime(df['CHSTOL'],errors='coerce')
#הוספת עמודות עזר עם חילוץ מעמודת התאריך
df['date'] = df['CHSTOL'].dt.date
df['hour'] = df['CHSTOL'].dt.hour
df['weekday'] = df['CHSTOL'].dt.dayofweek
df['weekday_name'] = df['CHSTOL'].dt.day_name()
df['month'] = df['CHSTOL'].dt.month
#מחיקת שורות שלא מהתאריך הספציפי של הניתוח
df = df[df['date'] == pd.to_datetime("2025-07-03").date()]
#ספירה כמה טיסות היו בכל שעה
flight_per_hour = df['hour'].value_counts().sort_index()
#ספירה איזה יעד הכי פופולרי
flights_by_destination = df["CHLOC1T"].value_counts()
#ספירה כמה טיסות כל חברה הפעילה
flights_by_operator = df['CHOPERD'].value_counts()

#בניית הגרף לפי שעות
def hour():
    st.header("Number of flights per hour")
    fig, ax = plt.subplots()
    ax.bar(flight_per_hour.index,flight_per_hour.values,color="skyblue")
    ax.set_xlabel("Hour of the day")
    ax.set_ylabel("Number of flights")
    ax.set_title("Flights per hour")
    ax.set_xticks(range(0, 24))
    return fig
#יצירת הגרף לפי יעדים פופולריים
def popular():
    st.header("Popular destinations")
    fig, ax = plt.subplots(figsize=(8,8))
    ax.pie(flights_by_destination.values[:10],labels=flights_by_destination.index[:10],
            autopct='%1.1f%%',startangle=90,colors=plt.cm.tab20.colors)
    ax.set_title("Top 10 destinations")
    return fig
# יצירת הגרף לפי חברות פעילות
def active_airlines():
    st.header("The most active airlines")
    fig ,ax = plt.subplots(figsize=(8,8))
    ax.pie(flights_by_operator.values[:10],labels=flights_by_operator.index[:10],
            autopct='%1.1f%%',startangle=90,colors=plt.cm.Paired.colors)
    ax.set_title("Top 10 active airlines")
    return fig

#הגדרת משתנה המצב
if "selected_chart" not in st.session_state:
    st.session_state.selected_chart = None
#אופציה למשתמש לאתחל את התצוגה
reset_col = st.columns(3)[1]
with reset_col:
    if st.button("🔁 Reset selection", key="reset_button"):
        st.session_state.selected_chart = None
        st.experimental_rerun()
st.write("---")
#כפתור ראשי
main_col = st.columns(3)
with main_col[1]:
    if st.button("Show All Charts"):
        st.session_state.selected_chart = "all"
st.write("---")
#כפתורים משניים
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Flights per hour"):
        st.session_state.selected_chart = "flights_per_hour"
with col2:
    if st.button("Popular destinations"):
        st.session_state.selected_chart = "popular_destinations"
with col3:
    if st.button("Most active airlines"):
        st.session_state.selected_chart = "active_airlines"

st.write("---")

#פונקציה להצגת הגרפים
def show_chart(chart_name, container):
    if chart_name == "flights_per_hour":
        with container:
            st.pyplot(hour())
    elif chart_name == "popular_destinations":
        with container:
            st.pyplot(popular())
    elif chart_name == "active_airlines":
        with container:
            st.pyplot(active_airlines())
#הפעלת התוכנית
if st.session_state.selected_chart == "all":
    col_a, col_b, col_c = st.columns(3)
    show_chart("flights_per_hour", col_a)
    show_chart("popular_destinations", col_b)
    show_chart("active_airlines", col_c)
elif st.session_state.selected_chart:
    col = st.container()
    show_chart(st.session_state.selected_chart, col)

#הצגת צילומסך מהטבלה המקורית
st.subheader("original table")
st.image("table_preview.png",caption="Taking a snapshot of the original table in the database",use_container_width =True)
