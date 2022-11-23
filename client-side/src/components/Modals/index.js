import React, { useState } from 'react';
import Button from 'react-bootstrap/Button';
import Modal from 'react-bootstrap/Modal';

const Modals = ({handleShow, show, handleClose, handleResetWorkspace}) => {
  return (
    <>
      <Button variant="primary" onClick={handleShow} style={{width: '180px'}}>
        Reset Workspace
      </Button>

      <Modal show={show} onHide={handleClose}>
        <Modal.Header closeButton>
          <Modal.Title>Reset Workspace</Modal.Title>
        </Modal.Header>
        <Modal.Body>Are you sure you want to restart? This will overwrite your files and reset your progress.</Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={handleClose}>
            Cancel
          </Button>
          <Button variant="primary" onClick={handleResetWorkspace}>
            Reset
          </Button>
        </Modal.Footer>
      </Modal>
    </>
  );
}

export default Modals;