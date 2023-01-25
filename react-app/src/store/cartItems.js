import { csrfFetch } from './csrf';

const POST_CART_ITEM = 'cartItem/POST_CART_ITEM';
const GET_CART_ITEMS = 'cartItem/GET_CART_ITEMS';
const PUT_CART_ITEM = 'cartItem/PUT_CART_ITEM';
const DELETE_CART_ITEM = 'cartItem/DELETE_CART_ITEM';
const CLEAR_CART = 'cartItem/CLEAR_CART';


export const postCartItem = (product_id, quantity) => async dispatch => {
    const response = await csrfFetch('/api/cart_items', {
        method: "POST",
        body: JSON.stringify({ product_id, quantity })
    });
    const cartItem = await response.json();
    dispatch({ type: POST_CART_ITEM, cartItem });
};

export const getCartItems = () => async dispatch => {
    console.log("getCartItems");
    const response = await csrfFetch(`/api/cart_items`);
    const cartItems = await response.json();
    dispatch({ type: GET_CART_ITEMS, cartItems });
};

export const putCartItem = (product_id, quantity) => async dispatch => {
    const response = await csrfFetch(`/api/cart_items`, {
        method: "PUT",
        body: JSON.stringify({ product_id, quantity })
    });
    const cartItem = await response.json();
    dispatch({ type: PUT_CART_ITEM, cartItem });
};

export const deleteCartItem = productId => async dispatch => {
    await csrfFetch(`/api/cart_items/${productId}`, { method: "DELETE" });
    dispatch({ type: DELETE_CART_ITEM, productId });
};

export const clearCart = () => async dispatch => {
    dispatch({ type: CLEAR_CART });
    await csrfFetch(`/api/cart_items`, { method: "DELETE" });
};

export default function cartItemReducer(state = {}, action) {
    const newState = { ...state };
    switch (action.type) {
        case POST_CART_ITEM:
            newState[action.cartItem.product_id] = action.cartItem.quantity;
            return newState;
        case GET_CART_ITEMS:
            for (const cartItem of action.cartItems) {
                newState[cartItem.product_id] = cartItem.quantity;
            }
            return newState;
        case PUT_CART_ITEM:
            newState[action.cartItem.product_id] = action.cartItem.quantity;
            return newState;
        case DELETE_CART_ITEM:
            delete newState[action.cartItem.product_id];
            return newState;
        case CLEAR_CART:
            return {};
        default:
            return state;
    }
};
