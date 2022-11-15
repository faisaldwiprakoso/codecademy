import React, {useState, useEffect} from "react";
import axios from "axios";
import Row from 'react-bootstrap/Row';
import Card from 'react-bootstrap/Card';
import Tab from 'react-bootstrap/Tab';
import Tabs from 'react-bootstrap/Tabs';
import Spinner from 'react-bootstrap/Spinner';

const baseURL = "http://127.0.0.1:8000/course/detail/";

const CourseDetail = () => {
	const [courseData, setCourseData] = useState({});
	const [isLoading, setIsLoading] = useState(true);
	const id = window.location.pathname.split("/").pop() + "/";

	useEffect(() => {
		axios.get(baseURL + id)
		.then(response => setCourseData(response.data)).then(() => setIsLoading(false))
		.catch((error) => {
			console.log(error);
		});
	}, []);

	
	return (
		<div>
			<h1>{courseData.course_name}</h1>
			{!isLoading ? 
				<Row key={id} style= {{marginTop :'20px'}}>
					<Tabs
					defaultActiveKey="overview"
					id="uncontrolled-tab-example"
					className="mb-3"
					>
						<Tab eventKey="overview" title="Overview">
							<Card>
								<Card.Body>
									<Card.Title>{courseData.course_description}</Card.Title>
								</Card.Body>
							</Card>
						</Tab>
						<Tab eventKey="syllabus" title="Syllabus">
							{courseData.courses_task.map((data,id)=>{
								return (
									<Row key={id}>
										<Card style={{marginTop: '20px'}}>
											<Card.Body>
												<Card.Title>{data.task_name}</Card.Title>
												<Card.Text>
													{data.task_description}
												</Card.Text>
												<Card.Link href={`/task-detail/${data.id}`}>Start Learning</Card.Link>
											</Card.Body>
										</Card>
									</Row>
								)
							})}
						</Tab>
					</Tabs>
				</Row>
				: 
				<Spinner animation="grow" />
			}
		</div>
	)
}

export default CourseDetail;