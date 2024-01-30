import streamlit as st
import requests
import json

#DOMAIN API HANDLER
PATH_DOMAIN = "https://velta-present-staging.deveureka.com/v1"

def queryIdParam():
    try:
        key = 'id'
        query_params= st.experimental_get_query_params()
        if query_params:
            student_id= query_params[key][0]
            return student_id
        else:
            st.error("The student 'id' query parameter is missing.")
            return None
    except Exception as e:
        st.error(f"An error occured: {e}")
        return None

def getStudents(student_id=queryIdParam()):
    return f"{PATH_DOMAIN}/students/{student_id}"

def postStudentsPresence(student_id=queryIdParam()):
    return f"{PATH_DOMAIN}/students/{student_id}/present"
class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data

def student_attendance(data):
    # CREATE FORM
    # Disabled field
    st.session_state["disabled"] = True

    st.markdown("<h2 style='text-align: center; color: black;'>Velta Academy</h2>", unsafe_allow_html=True)

    st.markdown("<h5 style='text-align: left; color: black;'>Student Attendance</h5>", unsafe_allow_html=True)
    
    # Student Information 
    studentId = st.text_input(label='ID', value= data['id'],key='studentId', disabled=st.session_state.disabled)
    studentName = st.text_input(label='Name', value= data['name'],key='studentName', disabled=st.session_state.disabled)
    totalPresent = st.text_input(label='Total Presence', value= data['totalPresent'],key='totalPresent', disabled=st.session_state.disabled)
    availableQouta = st.text_input(label='Available Attendance', value= data['availableQuota'],key='availableQuota', disabled=st.session_state.disabled)

    # Mentor Validation
    with st.form(key='my_form', clear_on_submit=True):
        st.markdown("<br> </h2>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: left; color: black;'>Mentor</h5>", unsafe_allow_html=True)

        mentorName = st.text_input(label='Name', key='mentorName')
        mentorPassword = st.text_input(label='Password', type='password', key='mentorPassword') 
        submitted = st.form_submit_button("Sumbit")
    # Display the input data when the form is submitted
    if submitted:
        # st.write(f'ID: {studentId}, Student Name: {studentName}, Total Presence: {totalAttendance}, Available Quota: {availableAttendance} by Mentor Name: {mentorName} with password: {mentorPassword}')
        
        form_data = {
        'username': mentorName,
        'password': mentorPassword
        }

        # Simulate a successful POST response
        post_response = MockResponse({"success": True, "message": "Presence Successfully", "data":form_data}, 200)

        # Post the data to the API
        post_response = requests.post(postStudentsPresence(), data=form_data)

        # Check if the post request was successful
        if post_response.status_code == 200:
            st.write('Presence Successfully')
        else:
            st.write('Failed to post data')

# GET DATA FROM API
# Hit the API
response = requests.get(getStudents())

# Check if the request was successful
if response.status_code == 200:
    # Convert the response to JSON
    data = response.json()
    student_attendance(data['data'])

else:
    st.write('Failed to get data from the API')

