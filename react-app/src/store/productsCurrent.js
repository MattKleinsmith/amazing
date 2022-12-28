import { csrfFetch } from './csrf';

const GET_CURRENT_PRODUCTS = 'productsCurrent/GET_CURRENT_PRODUCTS';
const DELETE_CURRENT_PRODUCT = 'productsCurrent/DELETE_CURRENT_PRODUCT';

export const getProductsCurrent = () => async dispatch => {
    const response = await csrfFetch('/api/products/current');
    const products = await response.json();
    dispatch({ type: GET_CURRENT_PRODUCTS, products });
};

export const deleteProductCurrent = productId => async dispatch => {
    dispatch({ type: DELETE_CURRENT_PRODUCT, productId });
};

export default function productsCurrentReducer(state = [], action) {
    switch (action.type) {
        case GET_CURRENT_PRODUCTS:
            return action.products;
        case DELETE_CURRENT_PRODUCT:
            return state.filter(product => product.id !== action.productId);
        default:
            return state;
    }
};
