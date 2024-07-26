import React, { useState } from 'react';
import JobDescriptionInput from './components/JobDescriptionInput';
import ProfileDisplay from './components/ProfileDisplay';

function App() {
    const [jobDescription, setJobDescription] = useState('');
    const [profiles, setProfiles] = useState('');

    const handleSubmit = async () => {
        const response = await fetch('/match', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ job_description: jobDescription }),
        });
        const data = await response.json();
        setProfiles(data);
    };

    return (
        <div>
            <JobDescriptionInput jobDescription={jobDescription} setJobDescription={setJobDescription} />
            <button onClick={handleSubmit}>Match Profiles</button>
            <ProfileDisplay profiles={profiles} />
        </div>
    );
}

export default App;
