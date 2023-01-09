import styles from "./Logo.module.css"

import { NavLink } from "react-router-dom"
import { useDispatch } from "react-redux"
import { setShouldClearSearchBar } from "../../../store/searchbar";

export default function Logo() {
    const dispatch = useDispatch();
    return (
        <NavLink className={styles.wrapper} to="/" style={{ textDecoration: 'none' }} onClick={() => dispatch(setShouldClearSearchBar(""))}>
            <img className={styles.logo} src="/images/logo_white.png" alt="logo_white" />
            <div className={styles.prime} />
        </NavLink>
    )
}
