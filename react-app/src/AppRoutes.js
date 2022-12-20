import { Route, Routes } from "react-router-dom";
import SearchResults from "./components/SearchResults/SearchResults";
import Listing from "./components/Listing/Listing";

export default function AppRoutes() {
    return (
        <Routes>
            <Route path="/" element={"Root path element"} />
            <Route path="/s" element={<SearchResults />} />
            <Route path="/listing/:productId" element={<Listing />} />
        </Routes>
    );
}
