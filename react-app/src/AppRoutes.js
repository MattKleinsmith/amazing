import { Route, Routes } from "react-router-dom";

import SearchResults from "./components/SearchResults/SearchResults";
import Listing from "./components/Listing/Listing";
import SignInForm from "./components/SignInForm/SignInForm";
import RegisterForm from "./components/RegisterForm/RegisterForm";
import Homepage from "./components/Homepage/Homepage";
import Inventory from "./components/Inventory/Inventory";
import ListingForm from "./components/ListingForm/ListingForm";
import ReviewForm from "./components/ReviewForm/ReviewForm";
import AddressForm from "./components/AddressForm/AddressForm";
import Addresses from "./components/Addresses/Addresses";
import Orders from "./components/Orders/Orders";
import OrderConfirmation from "./components/OrderConfirmation/OrderConfirmation";
import Protected from "./components/Protected";
import Cart from "./components/Cart/Cart";

export default function AppRoutes() {
    return (
        <Routes>
            <Route path="/" element={<Homepage />} />

            <Route path="/s" element={<SearchResults />} />
            <Route path="/listing/:productId" element={<Listing />} />

            <Route path="/signin" element={<SignInForm />} />
            <Route path="/register" element={<RegisterForm />} />

            <Route path="/inventory" element={<Protected><Inventory /></Protected>} />
            <Route path="/inventory/add" element={<Protected><ListingForm /></Protected>} />
            <Route path="/inventory/:productId" element={<Protected><ListingForm /></Protected>} />

            <Route path="/addresses" element={<Protected><Addresses /></Protected>} />
            <Route path="/addresses/add" element={<Protected><AddressForm /></Protected>} />
            <Route path="/addresses/:addressId" element={<Protected><AddressForm /></Protected>} />

            <Route path="/orders" element={<Protected><Orders /></Protected>} />
            <Route path="/order-confirmation" element={<Protected><OrderConfirmation /></Protected>} />
            <Route path="/reviews/:productId" element={<Protected><ReviewForm /></Protected>} />

            <Route path="/cart" element={<Protected><Cart /></Protected>} />
        </Routes>
    );
}
