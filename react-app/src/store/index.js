import { createStore, combineReducers, applyMiddleware, compose } from "redux";
import thunk from "redux-thunk";
import sessionReducer from "./session";
import productsReducer from "./products";
import uiReducer from "./ui";
import productDetailsReducer from "./productDetails";
import productsCurrentReducer from "./productsCurrent";
import addressesReducer from "./addresses";
import ordersReducer from "./orders";
import reviewsReducer from "./reviews";

const rootReducer = combineReducers({
    session: sessionReducer,
    products: productsReducer,
    ui: uiReducer,
    productDetails: productDetailsReducer,
    productsCurrent: productsCurrentReducer,
    addresses: addressesReducer,
    orders: ordersReducer,
    reviews: reviewsReducer,
});

let enhancer;

if (process.env.NODE_ENV === "production") {
    enhancer = applyMiddleware(thunk);
} else {
    const logger = require("redux-logger").default;
    const composeEnhancers =
        window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
    enhancer = composeEnhancers(applyMiddleware(thunk, logger));
}

const configureStore = (preloadedState) => {
    return createStore(rootReducer, preloadedState, enhancer);
};

export default configureStore;
