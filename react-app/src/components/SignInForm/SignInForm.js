import styles from './SignInForm.module.css';
import { useState } from "react";
import { useDispatch } from "react-redux";
import * as sessionActions from "../../store/session";
import { NavLink } from 'react-router-dom';

export default function SignInForm() {
    const dispatch = useDispatch();
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [errors, setErrors] = useState([]);
    const [showPasswordField, setShowPasswordField] = useState(false);

    const handleSubmit = (e) => {
        e.preventDefault();
        setErrors([]);
        return dispatch(sessionActions.signIn({ email, password }))
            .catch(e => {
                const errors = Object.entries(e.errors).map(([errorField, errorMessage]) => `${errorField}: ${errorMessage}`);
                setErrors(errors);
            });
    };

    const onClickContinue = () => {
        console.log("continue");
    }

    return (
        <>
            <div className={styles.wrapper} >
                <NavLink className={styles.logo} to="/" style={{ textDecoration: 'none' }}>
                    <img src="/images/logo_black.png" alt="logo_black" />
                </NavLink>
                <form className={styles.form} onSubmit={handleSubmit}>
                    <div className={styles.signinHeader}>
                        <div className={styles.signIn}>Sign in</div>
                    </div>
                    {
                        errors.length > 0 && <ul className={styles.formErrors}>
                            {errors.map((error, idx) => <li key={idx}>{error}</li>)}
                        </ul>
                    }
                    <div className={styles.emailWrapper}>
                        <label htmlFor="signUpEmail" className={styles.emailLabel}>Email</label>
                        <input id="signUpEmail" className={styles.emailField}
                            type="text"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                            required
                        />
                    </div>

                    {showPasswordField && <label>
                        Password <br />
                        <input
                            className="field"
                            type="password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            required
                        />
                    </label>}

                    <div className={`${styles.continue} ${styles.noselect}`} onClick={onClickContinue}>Continue</div>

                    <div className={styles.terms}>By continuing, you agree to Amazing's <NavLink>You Must Hire Me Conditions</NavLink> and <NavLink>Just Kidding Notice</NavLink>.</div>
                    <div className={styles.demoWrapper}>
                        <div className={styles.rightArrow} />
                        <div type="submit" className={styles.demo} onClick={() => {
                            setEmail("email@email.com");
                            setPassword("password");
                        }}>Sign in as demo user?</div>
                    </div>
                </form>

                <div className={styles.newWrapper}>
                    <div className={styles.line}>
                        <div className={styles.new}>New to Amazing?</div>
                    </div>
                    <div className={styles.create}>Create your Amazing account</div>
                </div>

            </div>

            <div className={styles.footer}>
                <div className={styles.footerLine} />
                <div className={styles.links}>
                    <a href="https://www.linkedin.com/in/matthewkleinsmith/">LinkedIn</a>
                    <a href="https://github.com/MattKleinsmith/">GitHub</a>
                    <a href="https://github.com/MattKleinsmith/amazing/">Project repo</a>
                </div>
                <div className={styles.copyright}>
                    Capstone project by <a href="https://github.com/MattKleinsmith/">Matt Kleinsmith</a> of App Academy
                </div>
            </div>
        </>
    );
}
