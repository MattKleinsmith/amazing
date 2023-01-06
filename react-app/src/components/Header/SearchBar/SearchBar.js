import styles from "./SearchBar.module.css";

import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate } from "react-router";
import { useSearchParams } from "react-router-dom";

import { setKeywords } from "../../../store/keywords";

export default function SearchBar() {
    const dispatch = useDispatch();
    const navigate = useNavigate();

    const searchParams = useSearchParams()[0];
    const keywords = useSelector(state => state.keywords);

    const newKeywords = searchParams.get('k');
    useEffect(() => {
        dispatch(setKeywords(newKeywords));
    }, [newKeywords, dispatch]);

    const handleSearch = async (e) => {
        if (e) e.preventDefault();
        if (keywords) {
            navigate(`/s?k=${keywords.replace(" ", "+")}`);
        } else {
            navigate("/");
        }
    }

    return (
        <div className={styles.wrapper}>
            <div className={styles.content}>
                <form onSubmit={handleSearch} className={styles.form}>
                    <input
                        type="text"
                        className={styles.searchBar}
                        value={keywords ? keywords : ""}
                        onChange={(e) => dispatch(setKeywords(e.target.value))}
                    />
                </form>
                <div onClick={handleSearch} className={`${styles.iconWrapperBase}`}>
                    <i className={`fa-solid fa-magnifying-glass ${styles.icon}`} />
                </div>
            </div>
        </div>
    )
}
