const SET_KEYWORDS = 'ui/setKeywords';

export const setKeywords = keywords => { return { type: SET_KEYWORDS, keywords }; };

export default function keywordsReducer(state = "", action) {
    switch (action.type) {
        case SET_KEYWORDS:
            return action.keywords
        default:
            return state;
    }
};
