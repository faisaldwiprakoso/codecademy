import React, {useState, useEffect} from "react";
import axios from "axios";
import parse from 'html-react-parser'
import CodeEditorWindow from "../../Editor";
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Button from 'react-bootstrap/Button';
import Spinner from 'react-bootstrap/Spinner';
import Modals from "../../Modals";


const baseURL = "http://127.0.0.1:8000/task/";
const basePostURL = "http://127.0.0.1:8000/solution/"

const TaskDetail = () => {
	const [detailTask, setDetailTask] = useState({});
	const [isLoading, setIsLoading] = useState(true)
	const [value, setValue] = useState('');
	const [solution, setSolution] = useState({});
	const [showModal, setShowModal] = useState(false);
	const [isError, setIsError] = useState(false)
	const id = window.location.pathname.split("/").pop() + "/";

	useEffect(() => {
    axios.get(baseURL + id).then(response => setDetailTask(response.data))
		.then(() => setIsLoading(false)).then(() => setValue(detailTask.default_code))
		.catch((error) => {
      console.log(error);
			setIsError(true);
    });
	}, [detailTask.default_code]);

	const handleEditorChange = (value) => {
    setValue(value);
  };

  const handleCompile = () => {
    const formData = {
			"status": true,
			"solution_code": value,
			"task": detailTask.id,
			"file_extension": detailTask.task_file_extension
    };
    const options = {
      method: "POST",
      url: basePostURL,
      data: formData,
    };

    axios
      .request(options)
      .then((response) => {
        console.log("res.data", response.data);
				setSolution(response.data);
      })
      .catch((err) => {
        let error = err.response ? err.response.data : err;
        // get error status
        let status = err.response.status;
        console.log("status", status);
        if (status === 429) {
          console.log("too many requests", status);

        }
        console.log("catch block...", error);
      });
  };

  const handleResetCode = () => {
		setValue(detailTask.default_code);
		setShowModal(false);
  }

  const handleCloseModal = () => setShowModal(false);
  const handleShowModal = () => setShowModal(true);

	return (
		<div>
			{isError ? 
				<h1> Page is not available</h1>
			:
			!isLoading ? 
				<Row>
					<Col xs={4} md={4} style={{borderColor : 'black', borderStyle : 'solid'}}>
						<h3>{detailTask.task_name}</h3>
						<Row>
							{parse(detailTask.task_description)}
						</Row>
						<Row>
							<h3>Instruction</h3>
							{parse(detailTask.instruction)}
						</Row>
					</Col>
					<Col xs={4} md={4} style={{borderColor : 'black', borderStyle : 'solid'}}>
						<Row style={{ maxWidth: '100%', overflowX: 'hidden'}}>
							<CodeEditorWindow 
								language={`java`}
								code={value}
								handleChangeEditor={handleEditorChange}
							/>
						</Row>
						<Row style= {{marginTop: '20px', marginBottom: '10px'}}>
							<Col xs={2} md={2}>
								<Button variant="secondary" style={{width: '60px'}} onClick={handleCompile}>Run</Button>
							</Col>
							<Col xs={2} md={2}>
								<Button variant="primary" style={{width: '80px', marginLeft: '-10px'}} onClick={() => {navigator.clipboard.writeText(value)}}>Copy</Button>
							</Col>
							<Col xs={2} md={2}>
								<Modals 
									handleShow={handleShowModal} 
									handleClose={handleCloseModal} 
									show={showModal}
									handleResetWorkspace= {handleResetCode}
								/>
							</Col>
						</Row>
					</Col>
					<Col xs={4} md={4} style={{borderColor : 'black', borderStyle : 'solid'}}>
						<h3>{solution.result}</h3>
					</Col>
				</Row>
				:
				<Spinner animation="grow" />
		}
		</div>
	)
}

export default TaskDetail;