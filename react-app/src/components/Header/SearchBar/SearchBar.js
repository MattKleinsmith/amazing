import styles from "./SearchBar.module.css";

import { useEffect, useRef, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useLocation, useNavigate } from "react-router";
import { useSearchParams } from "react-router-dom";

import { setShouldClearSearchBar } from "../../../store/searchbar";

export default function SearchBar() {
    const dispatch = useDispatch();
    const navigate = useNavigate();
    const location = useLocation();

    const shouldClearSearchBar = useSelector(state => state.searchbar);

    const searchParams = useSearchParams()[0];
    const keywordsFromUrl = searchParams.get('k');
    const [keywords, setKeywords] = useState(keywordsFromUrl ? keywordsFromUrl : "");

    const formRef = useRef();
    const searchButtonRef = useRef();

    useEffect(() => {
        setKeywords(keywordsFromUrl ? keywordsFromUrl : "");
    }, [location, keywordsFromUrl]);

    useEffect(() => {
        if (shouldClearSearchBar) {
            setKeywords("");
            dispatch(setShouldClearSearchBar(false));
        }
    }, [shouldClearSearchBar, dispatch]);

    const handleSearch = async (e) => {
        if (e) e.preventDefault();
        if (keywords) {
            navigate(`/s?k=${keywords.replace(" ", "+")}`);
        } else {
            navigate("/");
        }
        formRef.current.classList.remove(styles.formFocus);
    }

    document.addEventListener("click", (e) => {
        if (!formRef.current) return;
        if (e.composedPath().includes(formRef.current) && !e.composedPath().includes(searchButtonRef.current))
            formRef.current.classList.add(styles.formFocus);
        else
            formRef.current.classList.remove(styles.formFocus);
    });

    return (
        <div className={styles.wrapper}>
            <form ref={formRef} onSubmit={handleSearch} className={styles.form}>
                <input
                    type="text"
                    spellCheck="false"
                    className={styles.searchBar}
                    value={keywords}
                    onChange={e => setKeywords(e.target.value)}
                />
                <div ref={searchButtonRef} onClick={handleSearch} className={`${styles.iconWrapperBase}`}>
                    <i className={`fa-solid fa-magnifying-glass ${styles.icon}`} />
                </div>
            </form>
        </div>
    )
}
