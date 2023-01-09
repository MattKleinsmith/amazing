import { NavLink } from "react-router-dom"
import styles from "./Logo.module.css"
import { useDispatch } from "react-redux"
import { setShouldClearSearchBar } from "../../../store/searchbar";

export default function Logo() {
    const dispatch = useDispatch();
    return (
        <NavLink className={styles.wrapper} to="/" style={{ textDecoration: 'none' }} onClick={() => dispatch(setShouldClearSearchBar(""))}>
            <img src="/images/logo_white.png" alt="logo_white" />
        </NavLink>
    )
}
