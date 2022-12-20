const SET_MOUSE_POSITION = 'ui/SET_MOUSE_POSITION';
const SET_HOVER_MODAL = 'ui/SET_HOVER_MODAL';


export const setMousePosition = mouse => {
    return { type: SET_MOUSE_POSITION, mouse };
};

export const setHoverModal = hoverModal => {
    return { type: SET_HOVER_MODAL, hoverModal };
};

export default function uiReducer(state = {}, action) {
    const newState = { ...state };
    switch (action.type) {
        case SET_MOUSE_POSITION:
            newState.mouse = action.mouse;
            return newState;
        case SET_HOVER_MODAL:
            newState.hoverModal = action.hoverModal;
            return newState;
        default:
            return state;
    }
};
