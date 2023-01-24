import { csrfFetch } from './csrf';

const GET_ORDERS = 'orders/GET_ORDERS';
const CLEAR_ORDERS = 'orders/CLEAR_ORDERS';

export const clearOrders = () => {
    return { type: CLEAR_ORDERS };
}

export const postOrder = body => async dispatch => {
    const response = await csrfFetch('/api/orders', {
        method: "POST",
        body: JSON.stringify(body)
    });
    const order = await response.json();
    await dispatch(getOrders());
    return order.id;
};

export const getOrders = () => async dispatch => {
    const response = await csrfFetch('/api/orders/current');
    const orders = await response.json();
    dispatch({ type: GET_ORDERS, orders });
};

export default function ordersReducer(state = [], action) {
    switch (action.type) {
        case GET_ORDERS:
            return action.orders;
        case CLEAR_ORDERS:
            return [];
        default:
            return state;
    }
};
