import React, {useState, useEffect} from "react";
import axios from "axios";
import parse from 'html-react-parser'
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Card from 'react-bootstrap/Card';
// import { useSelector, useDispatch } from 'react-redux'
// import { decrementCounter, incrementCounter } from './counterSlice'

const baseURL = "http://127.0.0.1:8000/course/list/";

const CourseList = () => {
	const [courseList, setCourseList] = useState([]);
	// const count = useSelector((state) => state.counter)
	// const user = useSelector((state) => state.user)
  
	// const dispatch = useDispatch()
	
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
										<Row>
											<Col xs={12} md={12}>
												{parse(data.course_description)}
											</Col>
										</Row>
										<Card.Link href={`/course-detail/${data.id}`}>View Detail Course</Card.Link>
									</Card.Body>
								</Card>
							</Col>
						</Row>
					)
				})}
				{/* <button
          aria-label="Increment value"
          onClick={() => dispatch(incrementCounter())}
        >
          Increment
        </button> */}
		</div>
	)
}

// export default connect(mapStateToProps, mapDispatchToProps)(CourseList)
export default CourseList