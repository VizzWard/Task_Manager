import React from 'react';
import { Container, Row, Col, Button } from 'reactstrap';
import '../components/components.css'

function Welcome() {
  return (
    <div>
      <Container>
        <Row>
          <Col className="mainContainer">
            <div className="">
              <h2>Gestor de Tareas</h2>
              <p>Organiza tus tareas en un sencillo formulario</p>
              <Button href="/login" className="main-btn">Registrate Aquí</Button>
            </div>
          </Col>
        </Row>
        {/* <Row>
          <Col>
            <h2>Funcionalidades</h2>
            <img src="https://assets.dryicons.com/uploads/icon/svg/6512/d4d0b018-2bfc-409e-aa86-53754658f61a.svg" height="150"/> 
          </Col>
          <Col>
            <p>Aqui van las descripciones de las funcionalidades y la forma en la que podemos converser al usuario de usar nuestro sitio web</p>
          </Col>
        </Row>
        <Row>
          <Col>
            <p>Texto Plano</p>
          </Col>
          <Col>
          <h2>Beneficios</h2>
          </Col>
        </Row> */}
      </Container>
      
      
    </div>
  );
}

export default Welcome;