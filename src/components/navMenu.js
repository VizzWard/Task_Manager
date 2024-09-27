import React from "react";
import {  } from "react-router-dom";
import { Navbar, NavbarBrand, NavLink } from "reactstrap";

import './components.css'

function NavMenu(){

    return(
        <div>
            <Navbar className="mainNavbar">
                <NavbarBrand  className="btnHome" href='/'>Home</NavbarBrand>
                
                <NavLink href='login'>Inicia Sesion</NavLink>
                    
            </Navbar>
        </div>
    );
}

export default NavMenu;