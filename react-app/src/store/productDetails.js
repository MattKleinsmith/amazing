import { csrfFetch } from './csrf';

const GET_PRODUCT = 'products/GET_INDIVIUDAL_PRODUCT';

export const getProduct = (productId) => async dispatch => {
    const response = await csrfFetch(`/api/products/${productId}`);
    const product = await response.json();
    dispatch({ type: GET_PRODUCT, product });
};

export default function productDetailsReducer(state = {}, action) {
    const newState = { ...state };
    switch (action.type) {
        case GET_PRODUCT:
            newState[action.product.id] = action.product;
            return newState;
        default:
            return state;
    }
};
