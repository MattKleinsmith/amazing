import { csrfFetch } from './csrf';

const GET_PURCHASES = 'purchases/GET_PURCHASES';
const CLEAR_PURCHASES = 'purchases/CLEAR_PURCHASES';

export const clearPurchases = () => {
    return { type: CLEAR_PURCHASES };
}

export const postOrder = body => async dispatch => {
    const response = await csrfFetch('/api/orders', {
        method: "POST",
        body: JSON.stringify(body)
    });
    const order = await response.json();
    await dispatch(getPurchases());
    return order.id;
};

export const getPurchases = () => async dispatch => {
    const response = await csrfFetch('/api/purchases/current');
    const purchases = await response.json();
    dispatch({ type: GET_PURCHASES, purchases });
};

export default function purchasesReducer(state = [], action) {
    switch (action.type) {
        case GET_PURCHASES:
            return action.purchases;
        case CLEAR_PURCHASES:
            return [];
        default:
            return state;
    }
};
