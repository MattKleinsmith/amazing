import { csrfFetch } from './csrf';

const GET_PRODUCT = 'productDetails/GET_INDIVIDUAL_PRODUCT';
const POST_PRODUCT = 'productDetails/POST_INDIVIDUAL_PRODUCT';
const GET_PRODUCTS = 'productDetails/GET__PRODUCTS';

export const getProductDetails = (productId) => async dispatch => {
    const response = await csrfFetch(`/api/products/${productId}`);
    const product = await response.json();
    dispatch({ type: GET_PRODUCT, product });
};

export const getProductsDetails = (productIds) => async dispatch => {
    const response = await csrfFetch(`/api/products?product_ids=${productIds.join(',')}`);
    const products = await response.json();
    dispatch({ type: GET_PRODUCTS, products });
};


export const postProductDetails = (product) => async dispatch => {
    dispatch({ type: POST_PRODUCT, product });
};

export default function productDetailsReducer(state = {}, action) {
    const newState = { ...state };
    switch (action.type) {
        case GET_PRODUCT:
            newState[action.product.id] = action.product;
            return newState;
        case GET_PRODUCTS:
            for (const product of action.products) {
                newState[product.id] = product;
            }
            return newState;
        case POST_PRODUCT:
            newState[action.product.id] = action.product;
            return newState;
        default:
            return state;
    }
};
