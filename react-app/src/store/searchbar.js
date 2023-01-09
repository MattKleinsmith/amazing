const SET_SHOULD_CLEAR_SEARCH_BAR = 'searchbar/setShouldClearSearchBar';

export const setShouldClearSearchBar = shouldClearSearchBar => { return { type: SET_SHOULD_CLEAR_SEARCH_BAR, shouldClearSearchBar }; };

export default function searchbarReducer(state = false, action) {
    switch (action.type) {
        case SET_SHOULD_CLEAR_SEARCH_BAR:
            return action.shouldClearSearchBar
        default:
            return state;
    }
};
