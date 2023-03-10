import { csrfFetch } from './csrf';
import { getProductDetails, postProductDetails } from './productDetails';
import { deleteProductCurrent, postProductCurrent } from './productsCurrent';

const GET_PRODUCT = 'products/GET_INDIVIDUAL_PRODUCT';
const GET_PRODUCTS = 'products/GET_PRODUCTS';
const ADD_PRODUCT = 'products/ADD_PRODUCT';
const DELETE_PRODUCT = 'products/DELETE_PRODUCT';
const FILL_HOMEPAGE = 'products/FILL_HOMEPAGE';

export const getProducts = (size = 0, reverse = false) => async dispatch => {
    const response = await csrfFetch(`/api/products?size=${size}&reverse=${reverse}`);
    const products = await response.json();
    dispatch({ type: GET_PRODUCTS, products });
};

export const getProductsByKeywords = keywords => async dispatch => {
    const response = await csrfFetch(`/api/products?k=${keywords}`);
    const products = await response.json();
    dispatch({ type: GET_PRODUCTS, products });
};

export const getProductsForHomepage = () => async dispatch => {
    let phone = csrfFetch('/api/products?k=phone&size=4');
    let makeup = csrfFetch('/api/products?k=makeup&size=4');
    let basics = csrfFetch('/api/products?k=basics&size=4');
    const values = await Promise.all([phone, makeup, basics]);
    const data = await Promise.all(values.map(response => response.json()));
    dispatch({ type: FILL_HOMEPAGE, phone: data[0], makeup: data[1], basics: data[2] });
};

export const getProduct = (productId) => async dispatch => {
    const response = await csrfFetch(`/api/products/${productId}`);
    const product = await response.json();
    dispatch({ type: GET_PRODUCT, product });
};

export const postProduct = body => async dispatch => {
    const response = await csrfFetch('/api/products', {
        method: "POST",
        body: JSON.stringify(body)
    });
    const product = await response.json();
    dispatch({ type: ADD_PRODUCT, product });
    dispatch(postProductCurrent(product));
    dispatch(postProductDetails(product));
    return product.id;
};

export const putProduct = (productId, body) => async dispatch => {
    await csrfFetch(`/api/products/${productId}`, {
        method: "PUT",
        body: JSON.stringify(body)
    });
    dispatch(getProduct(productId));
    dispatch(getProductDetails(productId));
};

export const postProductImage = (productId, image, isPreview, position) => async dispatch => {
    const formData = new FormData();

    formData.append('image', image);
    formData.append('preview', isPreview);
    if (position) formData.append('position', position);

    const response = await fetch(`/api/products/${productId}/images`, {
        method: "POST",
        body: formData
    });

    if (response.status >= 400) {
        const errors = await response.json();
        console.log(errors);
        throw errors;
    }

    dispatch(getProductDetails(productId))
};

export const deleteProduct = productId => async dispatch => {
    await csrfFetch(`/api/products/${productId}`, { method: "DELETE" });
    dispatch({ type: DELETE_PRODUCT, productId });
    dispatch(deleteProductCurrent(productId));
};

export const deleteProductImage = (productId, productImageId) => async dispatch => {
    await csrfFetch(`/api/product_images/${productImageId}`, { method: "DELETE" });
    dispatch(getProductDetails(productId));
};

export default function productsReducer(state = { all: {}, filtered: {}, homepage: { phone: {}, makeup: {}, basics: {} } }, action) {
    const newState = { ...state };
    switch (action.type) {
        case GET_PRODUCTS:
            newState.filtered = {};
            for (const product of action.products) {
                newState.all[product.id] = product;
                newState.filtered[product.id] = product;
            }
            return newState;
        case FILL_HOMEPAGE:
            newState.homepage = { phone: {}, makeup: {}, basics: {} };
            for (const product of action.phone) {
                newState.homepage.phone[product.id] = product;
            }
            for (const product of action.makeup) {
                newState.homepage.makeup[product.id] = product;
            }
            for (const product of action.basics) {
                newState.homepage.basics[product.id] = product;
            }
            return newState;
        case ADD_PRODUCT:
            newState.all[action.product.id] = action.product;
            return newState;
        case GET_PRODUCT:
            newState.all[action.product.id] = action.product;
            return newState;
        case DELETE_PRODUCT:
            delete newState.all[action.productId];
            delete newState.filtered[action.productId];
            return newState;
        default:
            return state;
    }
};
