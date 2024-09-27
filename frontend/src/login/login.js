import React from "react";
import { AiFillApple } from "react-icons/ai";
import { FcGoogle } from "react-icons/fc";
import { Col, Container, Row, Form, FormGroup, Label, Input, Button } from "reactstrap";

function Login(){
    return(
        <Container fluid>
        <Row className="mainContainer">
          <Col md={6} className="d-flex align-items-center justify-content-center">
            <div>
              <h2>Bienvenido al organizador de tu vida</h2>
              <p>Probablemente una imagen de fondo</p>
              {/* 
              <img src="" alt="" className="img-fluid" />
              */}
            </div>
          </Col>
          <Col md={6} className="d-flex align-items-center justify-content-center">
            <Form className="w-75">
              <h3 className="text-center mb-4">Iniciar sesión</h3>
              <FormGroup>
                <Label for="email" className="labelLogin">Correo electrónico</Label>
                <Input type="email" name="email" id="email" placeholder="Ingrese su correo" />
              </FormGroup>
              <FormGroup>
                <Label for="password" className="labelLogin">Contraseña</Label>
                <Input type="password" name="password" id="password" placeholder="Ingrese su contraseña" />
              </FormGroup>
              <Button className="main-btn" block>Iniciar sesión</Button>
              <div className="loginServices">
                <Button className="btnServiceRound">
                    <FcGoogle size={20} className="mr-2"/>
                    Inicia con Google
                </Button>
                <Button className="btnServiceRound">
                    <AiFillApple size={20} className="mr-2"/>
                    Inicia con Apple
                </Button>
             </div>
             <p className="mt-3">¿No tienes cuenta? <a href="/register" className="linkColor">Registrate aquí</a></p>
            </Form>
          </Col>
        </Row>
      </Container>
    );
}

export default Login;