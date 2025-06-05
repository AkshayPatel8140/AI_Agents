import { Route, BrowserRouter as Router, Routes } from "react-router-dom";
import './App.css';
import { Dashboard } from '../src/pages/Dashboard.tsx';
import { Header } from './components/Header.tsx';
import { Chat } from '../src/pages/Chat.tsx';


function App() {
  return (
    <Router>
      <Header />
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/chat" element={<Chat />} />
      </Routes>
    </Router>
  );
}

export default App;
