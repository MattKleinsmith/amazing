import styles from "./SearchBar.module.css";
import { useState } from "react";
import { useNavigate } from "react-router";

export default function SearchBar() {
    const navigate = useNavigate();
    const [keywords, setKeywords] = useState("");

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
                        value={keywords}
                        onChange={(e) => setKeywords(e.target.value)}
                        placeholder="o_o" />
                </form>
                <div onClick={handleSearch} className={`${styles.iconWrapperBase}`}>
                    <i className={`fa-solid fa-magnifying-glass ${styles.icon}`} />
                </div>
            </div>
        </div>
    )
}
