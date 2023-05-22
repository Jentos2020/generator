import { BrowserRouter as Router, Routes, Route } from "react-router-dom"
import Monkeygen from "./components/docgen/Monkeygen";
import Footer from "./components/footer/Footer";
import Gen2fa from "./components/gen2fa/Gen2fa";
import Navbar from "./components/navbar/Navbar";
import Dashboard from "./components/dashboard/Dashboard";

function App() {
    return (
        <div className="App">
            <Router>
                <Navbar />
                <Routes>
                    <Route path="/" element={<Monkeygen />} />
                    <Route path="/2fa" element={<Gen2fa />} />
                    <Route path="/dashboard" element={<Dashboard />} />
                </Routes>
                <Footer />
            </Router>
        </div>
    );
}

export default App;
