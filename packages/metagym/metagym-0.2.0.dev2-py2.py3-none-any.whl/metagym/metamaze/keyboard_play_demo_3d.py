import gym
import metagym.metamaze

if __name__=='__main__':
    maze_env = gym.make("meta-maze-3D-v0", with_guidepost=False, max_steps=5000)
    cell_scale = 9
    task = maze_env.sample_task(cell_scale=cell_scale, cell_size=2.0, wall_height=3.2, allow_loops=True, crowd_ratio=0.35)
    maze_env.set_task(task)
    while True:
        maze_env.reset()
        done=False
        sum_reward = 0
        while not done:
            maze_env.render()
            state, reward, done, _ = maze_env.step(None)
            sum_reward += reward
        if(not maze_env.key_done):
            print("Episode is over! You got %.1f score."%sum_reward)
            maze_env.save_trajectory("trajectory_%dx%d.png"%(cell_scale, cell_scale))
            if(sum_reward > 0.0):
                cell_scale += 2 # gradually increase the difficulty
                print("Increase the difficulty, cell_scale = %d"%cell_scale)
            task = maze_env.sample_task(cell_scale=cell_scale, cell_size=2.0, wall_height=3.2, allow_loops=True, crowd_ratio=0.35)
            maze_env.set_task(task)
        else:
            break
