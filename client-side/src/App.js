import 'bootstrap/dist/css/bootstrap.min.css';
import Container from 'react-bootstrap/Container';
import NavbarComponent from './components/Navbar';
import About from './components/Pages/About';
import Home from './components/Pages/Home';
import Footer from './components/Footer';
import CourseList from './components/Pages/CourseList';
import CourseDetail from './components/Pages/CourseDetail';
import TaskDetail from './components/Pages/TaskDetail';
import { Route, Routes } from "react-router-dom";

function App(props) {
  return (
    <div className="App">
      <header className="App-header">
        <Container>
          <NavbarComponent/>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/about" element={<About />} />
            <Route path="/course-list" element={<CourseList />} />
            <Route path="/course-detail/:id" element={<CourseDetail />} />
            <Route path="/task-detail/:id" element={<TaskDetail />} />
          </Routes>
          <Footer/>
        </Container>
      </header>
    </div>
  );
}

export default App;
