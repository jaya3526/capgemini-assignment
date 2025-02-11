import logo from './logo.svg';
import './App.css';
import React, { useState } from "react";
const students = [
  {
    "StudentID": 101,
    "Name": "John Doe",
    "Age": 20,
    "Gender": "Male",
    "Class": "B.Sc. 1st Year",
    "ContactNumber": "9876543210",
    "EmailAddress": "johndoe@example.com"
  },
  {
    "StudentID": 102,
    "Name": "Jane Smith",
    "Age": 19,
    "Gender": "Female",
    "Class": "B.A. 2nd Year",
    "ContactNumber": "9876543211",
    "EmailAddress": "janesmith@example.com"
  },
  {
    "StudentID": 103,
    "Name": "Michael Johnson",
    "Age": 21,
    "Gender": "Male",
    "Class": "B.Com. 3rd Year",
    "ContactNumber": "9876543212",
    "EmailAddress": "michaeljohnson@example.com"
  },
  {
    "StudentID": 104,
    "Name": "Emily Davis",
    "Age": 22,
    "Gender": "Female",
    "Class": "M.Sc. 1st Year",
    "ContactNumber": "9876543213",
    "EmailAddress": "emilydavis@example.com"
  },
  {
    "StudentID": 105,
    "Name": "Chris Brown",
    "Age": 23,
    "Gender": "Male",
    "Class": "M.A. 2nd Year",
    "ContactNumber": "9876543214",
    "EmailAddress": "chrisbrown@example.com"
  },
  {
    "StudentID": 106,
    "Name": "Sophia Wilson",
    "Age": 20,
    "Gender": "Female",
    "Class": "B.Tech. 1st Year",
    "ContactNumber": "9876543215",
    "EmailAddress": "sophiawilson@example.com"
  },
  {
    "StudentID": 107,
    "Name": "David Miller",
    "Age": 21,
    "Gender": "Male",
    "Class": "M.Tech. 2nd Year",
    "ContactNumber": "9876543216",
    "EmailAddress": "davidmiller@example.com"
  },
  {
    "StudentID": 108,
    "Name": "Olivia Taylor",
    "Age": 22,
    "Gender": "Female",
    "Class": "B.Sc. 2nd Year",
    "ContactNumber": "9876543217",
    "EmailAddress": "oliviataylor@example.com"
  },
  {
    "StudentID": 109,
    "Name": "Daniel Martinez",
    "Age": 23,
    "Gender": "Male",
    "Class": "B.A. 3rd Year",
    "ContactNumber": "9876543218",
    "EmailAddress": "danielmartinez@example.com"
  },
  {
    "StudentID": 110,
    "Name": "Ava Anderson",
    "Age": 20,
    "Gender": "Female",
    "Class": "B.Com. 1st Year",
    "ContactNumber": "9876543219",
    "EmailAddress": "avaanderson@example.com"
  },
  {
    "StudentID": 111,
    "Name": "Ethan Thomas",
    "Age": 21,
    "Gender": "Male",
    "Class": "M.Sc. 2nd Year",
    "ContactNumber": "9876543220",
    "EmailAddress": "ethanthomas@example.com"
  },
  {
    "StudentID": 112,
    "Name": "Isabella Hernandez",
    "Age": 22,
    "Gender": "Female",
    "Class": "M.A. 1st Year",
    "ContactNumber": "9876543221",
    "EmailAddress": "isabellahernandez@example.com"
  },
  {
    "StudentID": 113,
    "Name": "James White",
    "Age": 23,
    "Gender": "Male",
    "Class": "B.Tech. 2nd Year",
    "ContactNumber": "9876543222",
    "EmailAddress": "jameswhite@example.com"
  },
  {
    "StudentID": 114,
    "Name": "Charlotte Lewis",
    "Age": 20,
    "Gender": "Female",
    "Class": "M.Tech. 1st Year",
    "ContactNumber": "9876543223",
    "EmailAddress": "charlottelewis@example.com"
  },
  {
    "StudentID": 115,
    "Name": "Benjamin Hall",
    "Age": 21,
    "Gender": "Male",
    "Class": "B.Sc. 3rd Year",
    "ContactNumber": "9876543224",
    "EmailAddress": "benjaminhall@example.com"
  }
]

function App() {
  const [searchvalue, setSearchValue] = useState("")
  const handlechange = (e) => {
    e.preventDefault();
    setSearchValue(e.target.value)
  }
  const studentsData=searchvalue.trim() === ""?students:
  students.filter((ele)=>ele.Name.toLowerCase().includes(searchvalue.toLowerCase()))
  return (
    <div>
      <center><h1>Students Info</h1></center>
      <input type="text" placeholder="enter the name" style={{width:"800px"}} onChange={handlechange} value={searchvalue} />
      <div>
        <table>
          <thead>
            <th>Id</th>
            <th>Name</th>
            <th>Age</th>
            <th>Gender</th>
            <th>Class</th>
            <th>ContactNumber</th>
            <th>Email</th>
          </thead>
          <tbody>
            {
              studentsData.map((student) => (
                <tr>
                  <td>{student.StudentID}</td>
                  <td>{student.Name}</td>
                  <td>{student.Age}</td>
                  <td>{student.Gender}</td>
                  <td>{student.Class}</td>
                  <td>{student.ContactNumber}</td>
                  <td>{student.EmailAddress}</td>
                </tr>
              ))
            }

          </tbody>
        </table>
      </div>
    </div>
  );
}

export default App;
