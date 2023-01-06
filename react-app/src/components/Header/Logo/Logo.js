import { NavLink } from "react-router-dom"
import styles from "./Logo.module.css"
import { useDispatch } from "react-redux"
import { setKeywords } from "../../../store/keywords";

export default function Logo() {
    const dispatch = useDispatch();
    return (
        <NavLink className={styles.wrapper} to="/" style={{ textDecoration: 'none' }} onClick={() => dispatch(setKeywords(""))}>
            <img src="/images/logo_white.png" alt="logo_white" />
        </NavLink>
    )
}
