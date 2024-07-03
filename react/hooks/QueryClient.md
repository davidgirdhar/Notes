### QueryClient

#### new QueryClient
    Usage: new QueryClient is used to create a new instance of the QueryClient class. This is typically done at a high level in your application, such as when setting up the React Query provider.
    
    Context: You create a QueryClient instance once and pass it to the QueryClientProvider, which then makes it available to all components in your application that use React Query hooks.

#### useQueryClient
    Usage: useQueryClient is a hook provided by React Query that allows you to access the QueryClient instance within any component that is a descendant of a QueryClientProvider.
    Context: It provides a way to interact with the QueryClient (e.g., invalidating queries, updating cache data) from within your components or hooks without needing to pass the client instance around manually.


```javascript
    // App.js
    import React from 'react';
    import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
    import MyComponent from './MyComponent';

    const queryClient = new QueryClient();

    function App() {
    return (
        <QueryClientProvider client={queryClient}>
        <MyComponent />
        </QueryClientProvider>
    );
    }

    export default App;

    // MyComponent.js
    import React from 'react';
    import { useQueryClient } from '@tanstack/react-query';

    function MyComponent() {
    const queryClient = useQueryClient();

    const handleUpdate = () => {
        queryClient.invalidateQueries('some-query-key');
    };

    return <button onClick={handleUpdate}>Update</button>;
    }

    export default MyComponent;
```

Now Using UseQueryClient is better than new QUeryClient as it updates the data more easily than new QueryClient