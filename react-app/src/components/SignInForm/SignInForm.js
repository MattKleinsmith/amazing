import styles from './SignInForm.module.css';
import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import * as sessionActions from "../../store/session";
import { NavLink, useNavigate } from 'react-router-dom';
import { useRef } from 'react';
import { useEffect } from 'react';

export default function SignInForm() {
    const dispatch = useDispatch();

    const [isLoaded, setIsLoaded] = useState(false);
    const user = useSelector(state => state.session.user);

    const emailField = useRef();
    const [email, setEmail] = useState("");
    const [emailError, setEmailError] = useState("");
    const [showEmailField, setShowEmailField] = useState(true);

    const passwordField = useRef();
    const [password, setPassword] = useState("");
    const [passwordError, setPasswordError] = useState("");
    const [showPasswordField, setShowPasswordField] = useState(false);

    const [bigError, setBigError] = useState("");

    const [terms1, setTerms1] = useState("");
    const [terms2, setTerms2] = useState("");

    const navigate = useNavigate();

    useEffect(() => {
        setIsLoaded(true);
    }, [setIsLoaded]);

    useEffect(() => {
        if (!isLoaded) return;
        if (showEmailField && emailField.current)
            emailField.current.focus();
        else if (passwordField.current)
            passwordField.current.focus();
    }, [showEmailField, showPasswordField, isLoaded]);

    const onClickContinue = () => {
        if (!email) {
            setEmailError("Enter your email");
            emailField.current.focus();
            return;
        }

        if (!validateEmail(email)) {
            setBigError("We cannot find an account with that email address.");
            return;
        }

        setEmailError("");
        setBigError("");
        setShowPasswordField(true);
        setShowEmailField(false);
    }

    const onClickSignIn = async () => {
        if (!password) {
            setPasswordError("Enter your password");
            passwordField.current.focus();
            return;
        }

        try {
            await dispatch(sessionActions.signIn({ email, password }));
            navigate("/");
        }
        catch (responseBody) {
            const backendErrors = Object.entries(responseBody.errors)
                .map(([errorField, errorMessage]) => `${errorField}: ${errorMessage}`);
            if (backendErrors.includes("Credentials: Email and password did not match")) {
                setBigError("Your password is incorrect");
            }
        }
    }

    const onClickChange = () => {
        setBigError("");
        setPasswordError("");
        setShowPasswordField(false);
        setShowEmailField(true);
    }

    const validateEmail = (email) => {
        const emailPattern = /\S+@\S+\.\S+/;
        return emailPattern.test(email);
    }

    const onSubmit = (e) => {
        e.preventDefault();
        showEmailField ? onClickContinue() : onClickSignIn();
    }

    if (!isLoaded) {
        return <>
            <NavLink className={styles.logo} to="/" style={{ textDecoration: 'none' }}>
                <img src="/images/logo_black.png" alt="logo_black" />
            </NavLink></>
    }

    if (user) {
        return <div className={styles.wrapper} >
            <NavLink className={styles.logo} to="/" style={{ textDecoration: 'none' }}>
                <img src="/images/logo_black.png" alt="logo_black" />
            </NavLink>
            <div>
                You are already logged in.
            </div>
        </div>
    }

    return (
        <>
            <div className={styles.wrapper} >

                <NavLink className={styles.logo} to="/" style={{ textDecoration: 'none' }}>
                    <img src="/images/logo_black.png" alt="logo_black" />
                </NavLink>

                {bigError && <div className={styles.problemWrapper}>
                    <div className={styles.problemIcon} />
                    <div className={styles.problemRight}>
                        <div className={styles.problemTitle}>There was a problem</div>
                        <div className={styles.problemText}>{bigError}</div>
                    </div>
                </div>}

                <form className={styles.form} onSubmit={onSubmit}>
                    <div className={styles.signinHeader}>
                        <div className={styles.signIn}>Sign in</div>
                    </div>
                    {showEmailField && <div className={styles.fieldWrapper}>
                        <label htmlFor="signUpEmail" className={styles.fieldLabel}>Email</label>
                        <input ref={emailField} id="signUpEmail" className={`${styles.fieldInput} ${emailError && styles.errorInput}`}
                            type="text"
                            value={email}
                            onChange={(e) => {
                                setEmail(e.target.value);
                                setEmailError("");
                            }}
                        />
                        {emailError && <div className={styles.errorWrapper}>
                            <div className={styles.errorIcon} />
                            <div className={styles.errorText}>{emailError}</div>
                        </div>}
                    </div>}

                    {showPasswordField && <div className={styles.email}>
                        <div>{email}</div>
                        <div className={styles.changeEmail} onClick={onClickChange}>Change</div>
                    </div>
                    }

                    {showPasswordField && <div className={styles.fieldWrapper}>
                        <label htmlFor="signUpPassword" className={styles.fieldLabel}>Password</label>
                        <input ref={passwordField} id="signUpPassword" className={`${styles.fieldInput} ${passwordError && styles.errorInput}`}
                            type="password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                        />
                        {passwordError && <div className={styles.errorWrapper}>
                            <div className={styles.errorIcon} />
                            <div className={styles.errorText}>{passwordError}</div>
                        </div>}
                    </div>}

                    {showEmailField && <div className={`${styles.continue} ${styles.noselect}`} onClick={onClickContinue}>Continue</div>}
                    {showPasswordField && <div className={`${styles.continue} ${styles.noselect}`} onClick={onClickSignIn}>Sign in</div>}

                    {showEmailField && <div className={styles.terms}>By continuing, you agree to Amazing's <NavLink onClick={() => setTerms1(true)}>You Must Hire Me Conditions</NavLink> and <NavLink onClick={() => setTerms2(true)}> Just Kidding Notice</NavLink>.</div>}

                    {terms1 && <div className={styles.jokeTerms}>There are no terms, I was just kidding.</div>}
                    {terms2 && <div className={styles.jokeTerms2}>Verily, there are no terms.</div>}


                    <div className={styles.demoWrapper}>
                        <div className={styles.rightArrow} />
                        <div type="submit" className={styles.demo} onClick={() => {
                            setEmail("email@email.com");
                            setPassword("password");

                            setEmailError("");
                            setBigError("");
                            setShowPasswordField(true);
                            setShowEmailField(false);
                        }}>Sign in as demo user?</div>
                    </div>
                </form>

                {showEmailField && <div className={styles.newWrapper}>
                    <div className={styles.line}>
                        <div className={styles.new}>New to Amazing?</div>
                    </div>
                    <div className={styles.create} onClick={() => {
                        navigate("/register");
                    }}>Create your Amazing account</div>
                </div>}

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
