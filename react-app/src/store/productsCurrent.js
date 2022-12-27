import { csrfFetch } from './csrf';

const GET_CURRENT_PRODUCTS = 'productsCurrent/GET_CURRENT_PRODUCTS';

export const getProductsCurrent = () => async dispatch => {
    const response = await csrfFetch('/api/products/current');
    const products = await response.json();
    dispatch({ type: GET_CURRENT_PRODUCTS, products });
};

export default function productsCurrentReducer(state = [], action) {
    switch (action.type) {
        case GET_CURRENT_PRODUCTS:
            return action.products;
        default:
            return state;
    }
};
