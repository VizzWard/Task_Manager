import './App.css';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

import Welcome from './welcome/welcome';
import NavMenu from './components/navMenu';
import Login from './login/login';



function App() {
  return (
    <BrowserRouter>
      <div className='backgroundContainer'>
        <NavMenu />
        <Routes>
          <Route path='/' element={<Welcome />} />
          <Route path='/login' element={<Login />} />
          <Route path='*' element={<did>404: Pagina no encontrada</did>} />
        </Routes>
      </div>
    </BrowserRouter>
    

  );
}

export default App;
