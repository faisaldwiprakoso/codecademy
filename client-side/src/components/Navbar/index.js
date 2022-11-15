import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';


const NavbarComponent = () => {
	return (
		<Navbar bg="light" expand="lg" sticky="top">
			<Container>
				<Navbar.Brand href="/">Simple Codecademy</Navbar.Brand>
				<Navbar.Toggle aria-controls="basic-navbar-nav" />
				<Navbar.Collapse id="basic-navbar-nav">
					<Nav className="me-auto">
						<Nav.Link href="/about">About</Nav.Link>
						<Nav.Link href="/course-list">Course List</Nav.Link>
					</Nav>
				</Navbar.Collapse>
			</Container>
		</Navbar>
	)
}

export default NavbarComponent;