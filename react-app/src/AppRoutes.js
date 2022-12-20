import { Route, Routes } from "react-router-dom";
import SearchResults from "./components/SearchResults/SearchResults";

export default function AppRoutes() {
    return (
        <Routes>
            <Route path="/" element={"Root path element"} />
            <Route path="/s" element={<SearchResults />} />
        </Routes>
    );
}
