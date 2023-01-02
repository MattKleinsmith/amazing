import { Route, Routes } from "react-router-dom";

import SearchResults from "./components/SearchResults/SearchResults";
import Listing from "./components/Listing/Listing";
import SignInForm from "./components/SignInForm/SignInForm";
import RegisterForm from "./components/RegisterForm/RegisterForm";
import Homepage from "./components/Homepage/Homepage";
import Inventory from "./components/Inventory/Inventory";
import ListingForm from "./components/ListingForm/ListingForm";
import AddressForm from "./components/AddressForm/AddressForm";
import Addresses from "./components/Addresses/Addresses";

export default function AppRoutes() {
    return (
        <Routes>
            <Route path="/" element={<Homepage />} />

            <Route path="/s" element={<SearchResults />} />
            <Route path="/listing/:productId" element={<Listing />} />

            <Route path="/signin" element={<SignInForm />} />
            <Route path="/register" element={<RegisterForm />} />

            <Route path="/inventory" element={<Inventory />} />
            <Route path="/inventory/add" element={<ListingForm />} />
            <Route path="/inventory/:productId" element={<ListingForm />} />

            <Route path="/addresses" element={<Addresses />} />
            <Route path="/addresses/add" element={<AddressForm />} />
            <Route path="/addresses/:addressId" element={<AddressForm />} />
        </Routes>
    );
}
