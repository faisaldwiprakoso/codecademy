import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';


const NavbarComponent = () => {
	return (
		<Navbar bg="dark" expand="lg" sticky="top">
			<Container>
				<Navbar.Brand href="/" style={{color: 'white', left: '10px', position: 'absolute'}}>Simple Codecademy</Navbar.Brand>
				<Navbar.Collapse id="basic-navbar-nav">
					<Nav className="me-auto">
						<Nav.Link href="/about" style={{color: 'white', left: '50px', position: 'relative'}}>About</Nav.Link>
						<Nav.Link href="/course-list" style={{color: 'white', left: '50px', position: 'relative'}}>Course List</Nav.Link>
					</Nav>
				</Navbar.Collapse>
			</Container>
		</Navbar>
	)
}

export default NavbarComponent;