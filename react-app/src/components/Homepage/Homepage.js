import SearchResults from "../SearchResults/SearchResults";
import styles from "./Homepage.module.css";

export default function Homepage() {
    return <div className={styles.wrapper}>
        <SearchResults keywords={"toothbrushes"} />
    </div>;
}
