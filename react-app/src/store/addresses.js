import { csrfFetch } from './csrf';

const POST_ADDRESS = 'addresses/POST_ADDRESS';
const GET_ADDRESSES = 'addresses/GET_ADDRESSES';
const PUT_ADDRESS = 'addresses/PUT_ADDRESS';
const DELETE_ADDRESS = 'addresses/DELETE_ADDRESS';

export const postAddress = body => async dispatch => {
    const response = await csrfFetch('/api/addresses', {
        method: "POST",
        body: JSON.stringify(body)
    });
    const address = await response.json();
    dispatch({ type: POST_ADDRESS, address });
    return address.id;
};

export const getAddresses = () => async dispatch => {
    const response = await csrfFetch('/api/addresses/current');
    const addresses = await response.json();
    dispatch({ type: GET_ADDRESSES, addresses });
};

export const putAddress = (addressId, body) => async dispatch => {
    const response = await csrfFetch(`/api/addresses/${addressId}`, {
        method: "PUT",
        body: JSON.stringify(body)
    });
    const address = await response.json();
    dispatch({ type: PUT_ADDRESS, address });
};

export const deleteAddress = addressId => async dispatch => {
    await csrfFetch(`/api/addresses/${addressId}`, {
        method: "DELETE"
    });
    dispatch({ type: DELETE_ADDRESS, addressId });
};

export default function addressesReducer(state = {}, action) {
    const newState = { ...state };
    switch (action.type) {
        case POST_ADDRESS:
            newState[action.address.id] = action.address;
            return newState;
        case GET_ADDRESSES:
            return action.addresses.reduce((newState, address) => {
                newState[address.id] = address;
                return newState;
            }, {});
        case PUT_ADDRESS:
            newState[action.address.id] = action.address;
            return newState;
        case DELETE_ADDRESS:
            delete newState[action.address.id];
            return newState;
        default:
            return state;
    }
};
