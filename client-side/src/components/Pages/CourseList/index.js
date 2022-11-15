import React, {useState, useEffect} from "react";
import axios from "axios";
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Card from 'react-bootstrap/Card';

const baseURL = "http://127.0.0.1:8000/course/list/";

const CourseList = () => {
	const [courseList, setCourseList] = useState([]);
	
	useEffect(() => {
    axios.get(baseURL).then(response => setCourseList(response.data))
		.catch((error) => {
      console.log(error);
    });
	}, []);

	return (
		<div>
				{courseList.map((data,id)=>{
					return (
						<Row key={id} style= {{marginTop :'20px'}}>
							<Col xs={12} md={12}>
								<Card>
									<Card.Body>
										<Card.Title>{data.course_name}</Card.Title>
										<Card.Text>
											{data.course_description}
										</Card.Text>
										<Card.Link href={`/course-detail/${data.id}`}>View Detail Course</Card.Link>
									</Card.Body>
								</Card>
							</Col>
						</Row>
					)
				})}
		</div>
	)
}

export default CourseList;