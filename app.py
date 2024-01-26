import streamlit as st
import requests
import json

GET_API= "https://mocki.io/v1/e5573ebb-6fe1-47d9-98ad-8f15acc29b0c"
# POST_API= ""

#Parse Query Params
# key = 'student_id'
# query_params= st.query_params.get_all(key)
# student_id= query_params[0]


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
    availableQuota = st.text_input(label='Available Attendance', value= data['availableQuota'],key='availableQuota', disabled=st.session_state.disabled)

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
        'studentId': studentId,
        'studentName': studentName,
        'totalAttendance': totalPresent,
        'availableAttendance': availableQuota,
        'mentorName': mentorName,
        'mentorPassword': mentorPassword
        }

        # Simulate a successful POST response
        post_response = MockResponse({"success": True, "message": "Presence Successfully", "data":form_data}, 200)

        # Check if the post request was successful
        if post_response.status_code == 200:
            print(post_response.json())
            # print('Presence Successfully')
            st.success('Presence Success!', icon="✅")
        else:
            print('Failed to post data')

        # Post the data to the API
        # post_response = requests.post(POST_API, data=form_data)

        # # Check if the post request was successful
        # if post_response.status_code == 200:
        #     st.write('Presence Successfully')
        # else:
        #     st.write('Failed to post data')

# GET DATA FROM API
# Hit the API
response = requests.get(GET_API)

# Check if the request was successful
if response.status_code == 200:
    # Convert the response to JSON
    data = response.json()
    student_attendance(data['data'])

else:
    st.write('Failed to get data from the API')

