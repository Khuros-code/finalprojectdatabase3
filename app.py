import streamlit as st
from sqlalchemy import text

list_gender = ['','male', 'female']
list_event_location_district = ['', 'al-Quds', 'Bethlehem', 'Deir al-Balah', 'East Jerusalem', 'Gaza','Gaza Strip','Gush Katif',
                                'Hebron','Israel','Jenin','Jericho','Khan Yunis','Nablus','North Gaza','Qalqiliya','Rafah',
                                'Ramallah and al-Bira','Salfit','Tubas','Tulkarm']

conn = st.connection("postgresql", type="sql", 
                     url="postgresql://ainisubagja:2winRbXv0lKL@ep-floral-poetry-94137080.us-east-2.aws.neon.tech/web")
with conn.session as session:
    query = text('CREATE TABLE IF NOT EXISTS FATALITIES (id serial, patient_name varchar, date_of_event date, age text, \
                                                       citizenship text, event_location text, event_location_district text, event_location_region text, \
                                                        date_of_death date, gender text, type_of_injury text);')
    session.execute(query)

st.header('FATALITIES IN THE ISRAEL-PALESTINIAN')
page = st.sidebar.selectbox("Pilih Menu", ["View Data","Edit Data"])

if page == "View Data":
    data = conn.query('SELECT * FROM fatalities ORDER By id;', ttl="0").set_index('id')
    st.dataframe(data)

if page == "Edit Data":
    if st.button('Tambah Data'):
        with conn.session as session:
            query = text('INSERT INTO fatalities (patient_name, date_of_event, age, citizenship, \
                         event_location, event_location_district, event_location_region, date_of_death, gender, type_of_injury) \
                          VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10);')
            session.execute(query, {'1':'', '2':None, '3':'', '4':'', '5':'', '6':'', '7':'', '8':None, '9':'', '10':''})
            session.commit()

    data = conn.query('SELECT * FROM fatalities ORDER By id;', ttl="0")
    for _, result in data.iterrows():        
        id = result['id']
        patient_name_lama = result["patient_name"]
        date_of_event_lama = result["date_of_event"]
        age_lama = result["age"]
        citizenship_lama = result["citizenship"]
        event_location_lama = result["event_location"]
        event_location_district_lama = result["event_location_district"]
        event_location_region_lama = result["event_location_region"]
        date_of_death_lama = result["date_of_death"]
        gender_lama = result["gender"]
        type_of_injury_lama = result["type_of_injury"]

        with st.expander(f'a.n. {patient_name_lama}'):
            with st.form(f'data-{id}'):
                patient_name_baru = st.text_input("patient_name", patient_name_lama)
                date_of_event_baru = st.date_input("date_of_event", date_of_event_lama)
                age_baru = st.text_input("age", age_lama)
                citizenship_baru = st.text_input("citizenship", citizenship_lama)
                event_location_baru = st.text_input("event_location", event_location_lama)
                event_location_district_baru = st.selectbox("event_location_district", list_event_location_district, list_event_location_district.index(event_location_district_lama))
                event_location_region_baru = st.text_input("event_location_region", event_location_region_lama)
                date_of_death_baru = st.date_input("date_of_death", date_of_death_lama)
                gender_baru = st.selectbox("gender", list_gender, list_gender.index(gender_lama))
                type_of_injury_baru = st.text_input("type_of_injury", type_of_injury_lama)
              
                
                col1, col2 = st.columns([1, 6])

                with col1:
                    if st.form_submit_button('UPDATE'):
                        with conn.session as session:
                            query = text('UPDATE fatalities \
                                          SET patient_name=:1, date_of_event=:2, age=:3, citizenship=:4, \
                                          event_location=:5, event_location_district=:6, event_location_region=:7, date_of_death=:8,\
                                          gender=:9, type_of_injury=:10\
                                          WHERE id=:11;')
                            session.execute(query, {'1':patient_name_baru, '2':date_of_event_baru, '3':age_baru, '4':citizenship_baru, 
                                                    '5':event_location_baru, '6':event_location_district_baru, '7':event_location_region_baru, '8':date_of_death_baru, '9':gender_baru,
                                                    '10':type_of_injury_baru, '11':id })
                            session.commit()
                            st.experimental_rerun()
                
                with col2:
                    if st.form_submit_button('DELETE'):
                        query = text(f'DELETE FROM fatalities WHERE id=:1;')
                        session.execute(query, {'1':id})
                        session.commit()
                        st.experimental_rerun()